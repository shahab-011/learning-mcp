"""Discover and call a stdio MCP server through LangChain."""

import asyncio
import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    server = Path(__file__).with_name("first_mcpserver_stdio_demo.py")
    client = MultiServerMCPClient(
        {
            "chapter_one": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(server)],
            }
        }
    )
    tools = await client.get_tools()
    print("Available tools:", ", ".join(tool.name for tool in tools))
    greet_tool = next(tool for tool in tools if tool.name == "greet")
    print("Tool result:", await greet_tool.ainvoke({"name": "LangChain"}))


if __name__ == "__main__":
    asyncio.run(main())
