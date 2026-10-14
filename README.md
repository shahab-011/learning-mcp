# MCP Learning Lab

A hands-on collection of Model Context Protocol (MCP) examples covering server tools, stdio and Streamable HTTP transports, Python and LangChain clients, community integrations, a reusable Python package, a gateway, and Docker.

The local examples use deterministic sample data and do not need API keys. The Tavily example needs a Tavily API key; the community DuckDuckGo example downloads its server with `uvx` the first time it runs.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)
- Node.js and npm (for the included JavaScript MCP SDK dependency)
- Docker Desktop (only for the Docker chapter)

## Install

From the project root in PowerShell:

```powershell
uv sync
npm install
```

The Python dependencies are installed in the project-local `.venv`. Run Python examples with `uv run python`; this automatically uses the project environment.

## Learning path

| Topic | Example |
| --- | --- |
| Create a tool server with FastMCP | `uv run python .\1_create_mcp\first_mcp_server_demo.py` |
| Connect with the official Python MCP SDK | `uv run python .\1_create_mcp\python_client_demo.py` |
| Connect with LangChain | `uv run python .\1_create_mcp\langchain_client_demo.py` |
| Streamable HTTP server | `uv run python .\chapter_2_http_mcp\http_mcp_demo.py` |
| LangChain HTTP client | `uv run python .\chapter_2_http_mcp\langchain_client_demo.py` |
| Community DuckDuckGo MCP server | `uv run python .\chapter_3_third_party_mcps\community_mcp_demo.py` |
| Tavily hosted MCP server | `uv run python .\chapter_3_third_party_mcps\tavily_mcp_demo.py` |
| Package tools and tests | `uv run python .\chapter_4_pypi_mcp\client_demo.py` and `uv run python .\chapter_4_pypi_mcp\test_package_demo.py` |
| HTTP gateway that forwards stdio tools | `uv run python .\chapter_5_mcp_gateway\gateway_demo.py` |
| Dockerized HTTP server | See the Docker instructions below |

Run the HTTP server in one terminal, then its client in a second terminal. HTTP servers bind to `127.0.0.1` for local use.

## API-key example

Copy `.env.example` to `.env`, add your own Tavily key, then run the Tavily example. `.env` is ignored by Git; never publish a real key.

## Python package example

The package has its own project metadata and lockfile. To install and run it independently:

```powershell
uv sync --project .\mcp_pypi_demo
uv run --project .\mcp_pypi_demo python -m mcp_pypi_demo.server
```

## Docker

From the project root:

```powershell
docker build -t mcp-learning-lab .\chapter_6_mcp_docker
docker run --rm -p 8000:8000 mcp-learning-lab
```

The MCP endpoint is available at `http://localhost:8000/mcp`.

## Project map

- `1_create_mcp/`, `2_http_mcp/`: introductory implementations
- `chapter_1_create_mcp/` through `chapter_6_mcp_docker/`: chapter exercises
- `mcp_pypi_demo/`: installable package example
- `src/` and `main.py`: project welcome entry point

## Share your learning

Example LinkedIn caption:

> I built an MCP Learning Lab to explore how the Model Context Protocol connects AI applications with tools. The project covers stdio and Streamable HTTP servers, Python and LangChain clients, third-party integrations, packaging, gateways, and Docker. Building it helped me understand tool discovery, transport choices, and how reusable MCP servers fit into an application.  
>  
> Project: [add your repository link]

Add your repository URL and a screenshot or short demo before posting.
