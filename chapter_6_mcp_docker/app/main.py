"""MCP server used by the Docker chapter."""

import os

from fastmcp import FastMCP

mcp = FastMCP(
    name="MCP Learning Lab Docker",
    instructions="A container-ready MCP server with simple demo tools.",
)


@mcp.tool()
def container_info() -> dict[str, str]:
    """Describe the service running in the container."""
    return {
        "service": "MCP Learning Lab Docker",
        "transport": "streamable-http",
        "status": "ready",
    }


@mcp.tool()
def echo_message(message: str) -> str:
    """Return the supplied message to demonstrate a containerized tool call."""
    return message


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host=os.getenv("MCP_HOST", "0.0.0.0"),
        port=int(os.getenv("MCP_PORT", "8000")),
    )
