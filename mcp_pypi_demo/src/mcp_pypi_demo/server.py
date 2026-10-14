"""MCP server entry point for the installable example package."""

from fastmcp import FastMCP

from mcp_pypi_demo.logic import process_text

mcp = FastMCP(
    name="MCP PyPI Demo",
    instructions="An installable example package exposing one text-processing tool.",
)

mcp.tool()(process_text)


if __name__ == "__main__":
    mcp.run(transport="stdio")
