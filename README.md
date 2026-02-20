# Corpus MCP Server

A Model Context Protocol (MCP) server for the Corpus Tracker application. This server allows AI assistants (like Claude) to securely interact with your financial portfolio, enabling them to fetch holdings, analyze net worth, and manage transactions.

## Features

- **Portfolio Analytics**: Fetch net worth, asset allocation, and top holdings.
- **Asset Management**: List, add, and remove Gold and Stock holdings.
- **Finance Tracking**: Log income and expenses, view transaction history, and analyze cash flow.
- **Secure Authentication**: Uses API Key authentication to communicate with your Corpus Tracker backend.

## Available Tools

### Profile & Management
- `get_my_profile`: Get the current user's profile and settings.
- `list_corpora`: List all corpora (profiles) the user belongs to.

### Analytics
- `get_portfolio_summary`: Get aggregated net worth, asset breakdown, and liabilities.
- `get_top_holdings(limit)`: Get top holdings by value.
- `get_portfolio_history`: Get portfolio history.

### Gold Holdings
- `list_gold_holdings`: List all gold holdings.
- `add_gold_holding(weight_grams, purchase_price, purchase_date)`: Add a new gold holding.
- `delete_gold_holding(holding_id)`: Delete a gold holding by ID.
- `live_gold_price()`: Get live gold price.
- `history_of_gold_price(limit)`: Get history of gold price.

### Stock Holdings
- `list_stock_holdings`: List all stock holdings.
- `add_stock_holding(symbol, quantity, avg_price)`: Add a new stock holding.
- `update_stock_holding(holding_id, symbol, quantity, avg_price)`: Update an existing stock holding.
- `delete_stock_holding(holding_id)`: Delete a stock holding by ID.
- `live_stock_price(symbol)`: Get live stock price.
- `history_of_stock_price(symbol, limit)`: Get history of stock price.

### Financial Transactions
- `list_transactions(start_date, end_date, category, type, limit)`: List transactions with filters.
- `add_transaction(type, amount, category, description, date)`: Add a new income or expense transaction.
- `delete_transaction(txn_id)`: Delete a transaction by ID.
- `get_cashflow_trend(days)`: Get income vs expense trend for the last N days.

### Stock Transactions
- `search_stock_symbol(query)`: Search for stock symbols.
- `add_stock_transaction(symbol, holding_id, transaction_type, quantity, price_per_share, transaction_date, notes)`: Add a new stock transaction.

### Mutual Fund Holdings
- `list_mutual_fund_holdings`: List all mutual fund holdings.

### Emergency Fund Management
- `list_emergency_fund_holdings`: List all emergency fund holdings.
- `add_emergency_fund_contribution(amount, date, source, notes)`: Add a new emergency fund contribution.

## Installation

```bash
pip install corpus-mcp
```

## Configuration

The server requires two environment variables to connect to your backend:

- `API_URL`: The URL of your Corpus Tracker backend API (e.g., `https://my-corpus.vercel.app/api/v1`).
- `API_KEY`: Your personal API Key generated from the Corpus Tracker settings.

## Usage

### Running Standalone

You can run the server directly:

```bash
# Set environment variables
export API_URL="https://my-corpus.vercel.app/api/v1"
export API_KEY="sk_..."

# Run the server
corpus-mcp
```

### Using with Claude Desktop

Add the following configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "corpus-tracker": {
      "command": "uvx",
      "args": [
        "corpus-mcp"
      ],
      "env": {
        "API_URL": "https://my-corpus.vercel.app/api/v1",
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
corpus-mcp
```

## License

MIT
