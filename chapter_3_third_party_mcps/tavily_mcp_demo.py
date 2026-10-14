"""Connect to Tavily's hosted MCP server (requires a Tavily API key)."""

import asyncio
import json
import os
from urllib.parse import urlencode

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


async def main() -> None:
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set TAVILY_API_KEY in your environment or a local .env file before running this example."
        )

    client = MultiServerMCPClient(
        {
            "tavily": {
                "transport": "streamable_http",
                "url": f"https://mcp.tavily.com/mcp/?{urlencode({'tavilyApiKey': api_key})}",
            }
        }
    )
    tools = await client.get_tools()
    print("Available Tavily tools:", ", ".join(tool.name for tool in tools))
    search_tool = next((tool for tool in tools if "search" in tool.name.lower()), None)
    if search_tool is None:
        raise RuntimeError("Tavily MCP did not expose a search tool.")
    result = await search_tool.ainvoke({"query": "Model Context Protocol"})
    print("Search result:", json.dumps(result, ensure_ascii=True, default=str))


if __name__ == "__main__":
    asyncio.run(main())
