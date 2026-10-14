"""Call the installable MCP server package through the Python MCP SDK."""

import asyncio
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    package_root = project_root / "mcp_pypi_demo"
    package_source = package_root / "src"
    python_path = os.environ.get("PYTHONPATH")
    environment = os.environ.copy()
    environment["PYTHONPATH"] = os.pathsep.join(
        part for part in (str(package_source), python_path) if part
    )
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "mcp_pypi_demo.server"],
        env=environment,
        cwd=package_root,
    )
    async with stdio_client(parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Package tools:", ", ".join(tool.name for tool in tools.tools))
            result = await session.call_tool(
                "process_text", arguments={"text": "Reusable Python packages make MCP servers easier to share."}
            )
            if result.isError:
                raise RuntimeError(f"MCP tool call failed: {result.content}")
            print("Tool result:", result.content)


if __name__ == "__main__":
    asyncio.run(main())
