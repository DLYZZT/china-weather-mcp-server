import os
import json
import httpx
from mcp.server.fastmcp import FastMCP


api_key = os.getenv("AMAP_API_KEY")
mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get weather for a chinese city

    Args:
        city: Chinese city name
    """
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={city}"
    headers = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            data = response.json()['lives'][0]
            return json.dumps(data)
        except Exception:
            return None


if __name__ == "__main__":
    mcp.run(transport='stdio')