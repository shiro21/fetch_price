import requests
import json
from datetime import datetime

def fetch_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "ethereum", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    price = response.json()["ethereum"]["usd"]
    now = datetime.now().isoformat()

    # Save JSON
    json_data = {"price": price, "updated_at": now}
    with open("eth_price.json", "w") as f:
        json.dump(json_data, f, indent=2)

    # Save Markdown
    md_data = f"""# Ethereum 가격 피드

- **가격**: ${price}
- **업데이트 시간**: {now}
"""
    with open("eth_price.md", "w") as f:
        f.write(md_data)

if __name__ == "__main__":
    fetch_eth_price()
