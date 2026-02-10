import asyncio
import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.append(os.path.join(os.getcwd(), "src"))

from mcp_server.server import (
    get_my_profile, 
    list_corpora, 
    get_portfolio_summary, 
    list_gold_holdings, 
    list_stock_holdings,
    list_transactions,
    get_top_holdings
)

async def verify():
    print("Verifying Extended MCP Tools...")
    
    print("\n1. Testing get_my_profile:")
    try:
        profile = await get_my_profile()
        print(f"Success: {profile[:100]}...")
    except Exception as e:
        print(f"Failed: {e}")

    print("\n2. Testing list_corpora:")
    try:
        corpora = await list_corpora()
        print(f"Success: {corpora[:100]}...")
    except Exception as e:
        print(f"Failed: {e}")

    print("\n3. Testing get_portfolio_summary:")
    try:
        summary = await get_portfolio_summary()
        print(f"Success: {summary[:100]}..." if "error" not in summary else f"Error: {summary}")
    except Exception as e:
        print(f"Failed: {e}")

    print("\n4. Testing list_gold_holdings:")
    try:
        gold = await list_gold_holdings()
        print(f"Success: {gold[:100]}..." if "error" not in gold else f"Error: {gold}")
    except Exception as e:
        print(f"Failed: {e}")

    print("\n5. Testing list_transactions:")
    try:
        txns = await list_transactions(limit=5)
        print(f"Success: {txns[:100]}..." if "error" not in txns else f"Error: {txns}")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    asyncio.run(verify())
