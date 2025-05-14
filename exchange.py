import requests
from datetime import datetime
import uuid

def get_exchange_rate(from_currency: str, to_currency: str):
    url = f"https://economia.awesomeapi.com.br/json/last/{from_currency}-{to_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Error fetching exchange rate")
    
    data = response.json()
    key = f"{from_currency}{to_currency}"
    rate_info = data[key]

    return {
        "sell": float(rate_info["high"]),
        "buy": float(rate_info["low"]),
        "date": datetime.fromtimestamp(int(rate_info["timestamp"])).strftime("%Y-%m-%d %H:%M:%S"),
        "id-account": str(uuid.uuid4())
    }