"""A small stdio MCP server with two tools."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="MCP Learning Lab",
    instructions="A local example server for learning MCP tools over stdio.",
)


@mcp.tool()
def fetch_data(topic: str = "Model Context Protocol") -> dict[str, str]:
    """Return a small sample record for a topic."""
    return {"topic": topic, "source": "local demo", "status": "ready"}


@mcp.tool()
def process_data(text: str) -> dict[str, str | int]:
    """Summarize text with a reproducible local word count."""
    words = text.split()
    return {"summary": " ".join(words[:12]), "word_count": len(words)}


if __name__ == "__main__":
    mcp.run(transport="stdio")