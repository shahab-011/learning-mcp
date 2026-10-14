"""Discover and invoke a local MCP server through LangChain."""

import asyncio
import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    server = Path(__file__).with_name("first_mcp_server_demo.py")
    client = MultiServerMCPClient(
        {
            "learning_lab": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(server)],
            }
        }
    )
    tools = await client.get_tools()
    print("Available tools:", ", ".join(tool.name for tool in tools))
    process_tool = next(tool for tool in tools if tool.name == "process_data")
    result = await process_tool.ainvoke({"text": "LangChain can use tools exposed by an MCP server."})
    print("Tool result:", result)


if __name__ == "__main__":
    asyncio.run(main())