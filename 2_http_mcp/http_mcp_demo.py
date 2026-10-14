"""Run the introductory MCP server over Streamable HTTP."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="MCP HTTP Learning Lab",
    instructions="A local example server for learning MCP over Streamable HTTP.",
)


@mcp.tool()
def fetch_http(topic: str = "MCP") -> dict[str, str]:
    """Return a sample record for an HTTP-client example."""
    return {"topic": topic, "transport": "streamable-http"}


@mcp.tool()
def process_http(text: str) -> dict[str, str | int]:
    """Summarize text and return its word count."""
    words = text.split()
    return {"summary": " ".join(words[:12]), "word_count": len(words)}


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8050)