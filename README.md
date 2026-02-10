# Corpus MCP Server

A Model Context Protocol (MCP) server for the Corpus Tracker application. This server allows AI assistants (like Claude) to securely interact with your financial portfolio, enabling them to fetch holdings, analyze net worth, and manage transactions.

## Features

- **Portfolio Analytics**: Fetch net worth, asset allocation, and top holdings.
- **Asset Management**: List, add, and remove Gold and Stock holdings.
- **Finance Tracking**: Log income and expenses, view transaction history, and analyze cash flow.
- **Secure Authentication**: Uses API Key authentication to communicate with your Corpus Tracker backend.

## Installation

```bash
pip install corpus-mcp
```

## Configuration

The server requires two environment variables to connect to your backend:

- `API_URL`: The URL of your Corpus Tracker backend API (e.g., `http://localhost:8000/api/v1` or your production URL).
- `API_KEY`: Your personal API Key generated from the Corpus Tracker settings.

## Usage

### Running Standalone

You can run the server directly:

```bash
# Set environment variables
export API_URL="http://localhost:8000/api/v1"
export API_KEY="sk_..."

# Run the server
mcp-server
```

### Using with Claude Desktop

Add the following configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "corpus-tracker": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "corpus-mcp"
      ],
      "env": {
        "API_URL": "http://localhost:8000/api/v1",
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Development

To install dependencies and run locally:

```bash
# Install dependencies
pip install .

# Run dev server
mcp-server
```

## License

MIT
