"""Connect to the community DuckDuckGo MCP server using uvx."""

import asyncio
import json
import shutil

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    uvx = shutil.which("uvx")
    if uvx is None:
        raise RuntimeError(
            "uvx is required for this community-server example. "
            "Install uv from https://docs.astral.sh/uv/."
        )
    client = MultiServerMCPClient(
        {
            "duckduckgo": {
                "transport": "stdio",
                "command": uvx,
                "args": ["duckduckgo-mcp-server"],
            }
        }
    )
    tools = await client.get_tools()
    print("Available DuckDuckGo tools:", ", ".join(tool.name for tool in tools))
    search_tool = next((tool for tool in tools if "search" in tool.name.lower()), None)
    if search_tool is None:
        raise RuntimeError("The community server did not expose a search tool.")
    result = await search_tool.ainvoke({"query": "Model Context Protocol"})
    print("Search result:", json.dumps(result, ensure_ascii=True, default=str))


if __name__ == "__main__":
    asyncio.run(main())
