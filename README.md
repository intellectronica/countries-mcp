# Countries MCP Server

An MCP server that provides information about countries, including names, codes, capitals, currencies, languages, and regions.

## Features

- List all countries
- Search countries by name (common or official)
- Get country by ISO code (CCA2, CCA3, CCN3)
- Get country capital, currency, and languages
- Filter countries by region

## Deployment on FastMCP Cloud

This server is ready for deployment on [FastMCP Cloud](https://fastmcp.cloud/).

1.  Create a new project on FastMCP Cloud.
2.  Select this repository.
3.  Set the entrypoint to `server.py:mcp`.
4.  Deploy!

## Local Development

1.  Install dependencies:
    ```bash
    uv sync
    ```

2.  Run the server:
    ```bash
    uv run fastmcp dev server.py
    ```

3.  Inspect the server:
    ```bash
    uv run fastmcp inspect server.py
    ```

## Data Source

Country data is sourced from [mledoze/countries](https://github.com/mledoze/countries).
