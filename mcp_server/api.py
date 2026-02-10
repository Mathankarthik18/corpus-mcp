import httpx
import os
from dotenv import load_dotenv
from typing import Optional, Dict, Any, List

# Load environment variables
load_dotenv()

API_URL = os.getenv("API_URL", "https://my-corpus.vercel.app/api/v1")
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Warning: API_KEY not found in environment variables.")

async def make_request(method: str, endpoint: str, data: Optional[Dict] = None) -> Any:
    """Helper to make authenticated requests to the backend"""
    headers = {
        "X-API-Key": API_KEY,
        "bg-bypass-cache": "true" 
    }
    
    async with httpx.AsyncClient() as client:
        url = f"{API_URL}{endpoint}"
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=data)
            elif method.upper() == "PUT":
                response = await client.put(url, headers=headers, json=data)
            elif method.upper() == "DELETE":
                response = await client.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported method: {method}")
                
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP Error: {e.response.status_code}", "detail": e.response.text}
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

async def get_default_corpus_id() -> Optional[int]:
    """
    Fetch the user's corpora and return the ID of the first one.
    Most users have one corpus.
    """
    # Endpoint based on app/api/corpus.py: list_corpuses is at GET /
    # So path is /corpus/ 
    data = await make_request("GET", "/corpus/")
    
    if isinstance(data, list) and len(data) > 0:
        # data is list of CorpusSchema objects
        return data[0].get("id")
    
    return None
