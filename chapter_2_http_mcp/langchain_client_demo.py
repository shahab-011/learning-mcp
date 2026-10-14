"""Connect to the Chapter 2 HTTP server and invoke its summarize tool."""

import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

SERVER_URL = "http://127.0.0.1:8050/mcp"


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "chapter_two_http": {
                "transport": "streamable_http",
                "url": SERVER_URL,
            }
        }
    )
    tools = await client.get_tools()
    print("Available tools:", ", ".join(tool.name for tool in tools))
    summarize_tool = next(tool for tool in tools if tool.name == "summarize")
    result = await summarize_tool.ainvoke(
        {"text": "Streamable HTTP lets MCP clients connect to servers over HTTP."}
    )
    print("Tool result:", result)


if __name__ == "__main__":
    asyncio.run(main())
