from mcp.server.fastmcp import FastMCP
from typing import Optional, List, Dict, Any
from mcp_server.api import make_request, get_default_corpus_id

# Initialize FastMCP Server
mcp = FastMCP("Corpus Tracker")

async def get_corpus_id() -> int:
    """Helper to get default corpus ID or raise error"""
    corpus_id = await get_default_corpus_id()
    if not corpus_id:
        raise ValueError("No corpus found. Please create a corpus in the web app first.")
    return corpus_id

# --- Generic Tools ---

@mcp.tool()
async def get_my_profile() -> str:
    """Get the current user's profile and settings."""
    data = await make_request("GET", "/settings")
    return str(data)

@mcp.tool()
async def list_corpora() -> str:
    """List all corpora (profiles) the user belongs to."""
    data = await make_request("GET", "/corpus/")
    return str(data)

# --- Analytics & Summary ---

@mcp.tool()
async def get_portfolio_summary() -> str:
    """Get aggregated net worth, asset breakdown, and liabilities."""
    corpus_id = await get_corpus_id()
    data = await make_request("GET", f"/analytics/{corpus_id}/net-worth")
    return str(data)

@mcp.tool()
async def get_top_holdings(limit: int = 5) -> str:
    """Get top holdings by value."""
    corpus_id = await get_corpus_id()
    data = await make_request("GET", f"/analytics/{corpus_id}/top-holdings?limit={limit}")
    return str(data)

# --- Gold Operations ---

@mcp.tool()
async def list_gold_holdings() -> str:
    """List all gold holdings."""
    corpus_id = await get_corpus_id()
    data = await make_request("GET", f"/gold/{corpus_id}/holdings")
    return str(data)

@mcp.tool()
async def add_gold_holding(
    weight_grams: float,
    purchase_price: float,
    purchase_date: str 
) -> str:
    """
    Add a new gold holding.
    purchase_date: YYYY-MM-DD format
    """
    corpus_id = await get_corpus_id()
    payload = {
        "weight_grams": weight_grams,
        "purchase_price": purchase_price,
        "purchase_date": purchase_date
    }
    data = await make_request("POST", f"/gold/{corpus_id}/holdings", payload)
    return str(data)

@mcp.tool()
async def delete_gold_holding(holding_id: int) -> str:
    """Delete a gold holding by ID."""
    corpus_id = await get_corpus_id()
    data = await make_request("DELETE", f"/gold/{corpus_id}/holdings/{holding_id}")
    return str(data)

# --- Stock Operations ---

@mcp.tool()
async def list_stock_holdings() -> str:
    """List all stock holdings."""
    corpus_id = await get_corpus_id()
    data = await make_request("GET", f"/stocks/{corpus_id}/stocks")
    return str(data)

@mcp.tool()
async def add_stock_holding(
    symbol: str,
    quantity: float,
    avg_price: float
) -> str:
    """
    Add a new stock holding.
    symbol: Stock Symbol (e.g. RELIANCE.NS)
    """
    corpus_id = await get_corpus_id()
    payload = {
        "symbol": symbol,
        "quantity": quantity,
        "avg_price": avg_price
    }
    data = await make_request("POST", f"/stocks/{corpus_id}/stocks", payload)
    return str(data)

@mcp.tool()
async def update_stock_holding(
    holding_id: int,
    symbol: str,
    quantity: float,
    avg_price: float
) -> str:
    """Update an existing stock holding."""
    corpus_id = await get_corpus_id()
    payload = {
        "symbol": symbol,
        "quantity": quantity,
        "avg_price": avg_price
    }
    data = await make_request("PUT", f"/stocks/{corpus_id}/stocks/{holding_id}", payload)
    return str(data)

@mcp.tool()
async def delete_stock_holding(holding_id: int) -> str:
    """Delete a stock holding by ID."""
    corpus_id = await get_corpus_id()
    data = await make_request("DELETE", f"/stocks/{corpus_id}/stocks/{holding_id}")
    return str(data)

# --- Finance & Transactions ---

@mcp.tool()
async def list_transactions(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    category: Optional[str] = None,
    type: Optional[str] = None,
    limit: int = 20
) -> str:
    """
    List transactions with filters.
    Dates in YYYY-MM-DD.
    Type: 'income', 'expense', or 'all'.
    """
    corpus_id = await get_corpus_id()
    query_parts = [f"limit={limit}"]
    if start_date: query_parts.append(f"start_date={start_date}")
    if end_date: query_parts.append(f"end_date={end_date}")
    if category: query_parts.append(f"category={category}")
    if type: query_parts.append(f"type={type}")
    
    query_string = "&".join(query_parts)
    data = await make_request("GET", f"/finance/{corpus_id}/transactions?{query_string}")
    return str(data)

@mcp.tool()
async def add_transaction(
    type: str, 
    amount: float, 
    category: str, 
    description: Optional[str] = None,
    date: Optional[str] = None
) -> str:
    """
    Add a new income or expense transaction.
    type: "income" or "expense"
    """
    corpus_id = await get_corpus_id()
    payload = {
        "type": type.lower(),
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    data = await make_request("POST", f"/finance/{corpus_id}/transactions", payload)
    return str(data)

@mcp.tool()
async def delete_transaction(txn_id: int) -> str:
    """Delete a transaction by ID."""
    corpus_id = await get_corpus_id()
    data = await make_request("DELETE", f"/finance/{corpus_id}/transactions/{txn_id}")
    return str(data)

@mcp.tool()
async def get_cashflow_trend(days: int = 30) -> str:
    """Get income vs expense trend for the last N days."""
    corpus_id = await get_corpus_id()
    data = await make_request("GET", f"/finance/{corpus_id}/cashflow-trend?days={days}")
    return str(data)

def main():
    """Entry point for the MCP server."""
    mcp.run()

if __name__ == "__main__":
    main()
