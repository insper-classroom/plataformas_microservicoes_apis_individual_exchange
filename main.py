from fastapi import FastAPI, Depends
from auth import authenticate_user
from exchange import get_exchange_rate

app = FastAPI(title="Exchange API")

@app.get("/exchange/{from_currency}/{to_currency}")
def exchange(from_currency: str, to_currency: str, _: None = Depends(authenticate_user)):
    try:
        result = get_exchange_rate(from_currency.upper(), to_currency.upper())
        return result
    except Exception as e:
        return {"error": str(e)}