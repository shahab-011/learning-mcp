"""Chapter 1: create an MCP server using stdio transport."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="Chapter 1 MCP Server",
    instructions="A minimal stdio server for practicing MCP tool discovery and calls.",
)


@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must contain at least one non-space character")
    return f"Hello, {cleaned_name}! Your first MCP tool call worked."


@mcp.tool()
def count_words(text: str) -> dict[str, int]:
    """Count words in a text string."""
    return {"word_count": len(text.split())}


if __name__ == "__main__":
    mcp.run(transport="stdio")