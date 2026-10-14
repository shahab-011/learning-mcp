"""Use the official Python SDK to discover and call a local MCP server."""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    server = Path(__file__).with_name("first_mcpserver_stdio_demo.py")
    parameters = StdioServerParameters(command=sys.executable, args=[str(server)])
    async with stdio_client(parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", ", ".join(tool.name for tool in tools.tools))
            result = await session.call_tool("greet", arguments={"name": "MCP learner"})
            if result.isError:
                raise RuntimeError(f"MCP tool call failed: {result.content}")
            print("Tool result:", result.content)


if __name__ == "__main__":
    asyncio.run(main())
