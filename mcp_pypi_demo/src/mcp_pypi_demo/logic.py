"""Reusable business logic shared by the MCP server and its tests."""


def process_text(text: str) -> dict[str, str | int]:
    """Return a short preview and word count for non-empty text."""
    words = text.split()
    if not words:
        raise ValueError("text must contain at least one word")
    return {"summary": " ".join(words[:12]), "word_count": len(words)}
