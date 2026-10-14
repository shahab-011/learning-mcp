"""Chapter 2: expose MCP tools over Streamable HTTP."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="Chapter 2 HTTP MCP Server",
    instructions="An HTTP MCP server for learning Streamable HTTP transport.",
)


@mcp.tool()
def get_server_info() -> dict[str, str]:
    """Return a small description of this server."""
    return {"name": "Chapter 2 HTTP MCP Server", "transport": "streamable-http"}


@mcp.tool()
def summarize(text: str) -> dict[str, str | int]:
    """Return the first twelve words and the full word count."""
    words = text.split()
    return {"summary": " ".join(words[:12]), "word_count": len(words)}


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8050)
