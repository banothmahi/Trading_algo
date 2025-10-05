# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Algo Trader API")

class RunRequest(BaseModel):
    symbol: str
    strategy: str  # 'sma' or 'rsi'

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run_strategy")
def run_strategy(req: RunRequest):
    # For a complete implementation, this endpoint would:
    # 1. fetch historical data for `req.symbol` (yfinance / exchange API)
    # 2. choose strategy module and run backtest, return metrics & signals
    # Here we return a placeholder message
    return {"message": f"Received request to run {req.strategy} for {req.symbol}. Implement data fetch & runner."}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
