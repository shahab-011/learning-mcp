"""Expose the Chapter 1 stdio server through a Streamable HTTP gateway."""

import sys
from pathlib import Path

from fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_SERVER = ROOT / "chapter_1_create_mcp" / "first_mcpserver_stdio_demo.py"

gateway = FastMCP(
    name="MCP Learning Lab Gateway",
    instructions="A small HTTP gateway that forwards tools from the Chapter 1 stdio server.",
)
chapter_server_proxy = FastMCP.as_proxy(
    {
        "mcpServers": {
            "chapter_one": {
                "command": sys.executable,
                "args": [str(CHAPTER_SERVER)],
            }
        }
    }
)
gateway.mount(chapter_server_proxy, prefix="chapter_one")


if __name__ == "__main__":
    gateway.run(transport="streamable-http", host="127.0.0.1", port=8060)
