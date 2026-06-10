from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Forex Trading API",
    description="EMA Crossover Automated Trading System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class OpportunityResponse(BaseModel):
    pair: str
    direction: str
    entry_price: float
    stop_loss: float
    take_profit: float
    confidence: float
    timestamp: datetime

class BacktestResult(BaseModel):
    pair: str
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    avg_win: float
    avg_loss: float
    sharpe_ratio: float
    max_drawdown: float
    profit_factor: float

class OperationResponse(BaseModel):
    id: int
    pair: str
    direction: str
    entry_price: float
    entry_time: datetime
    status: str
    pnl: Optional[float] = None

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}

@app.get("/opportunities", response_model=List[OpportunityResponse])
async def get_opportunities():
    """Get current trading opportunities"""
    # TODO: Fetch from database
    return []

@app.get("/backtest/{pair}", response_model=BacktestResult)
async def get_backtest_results(pair: str):
    """Get backtesting results for a specific pair"""
    # TODO: Fetch from database
    raise HTTPException(status_code=404, detail="Pair not found")

@app.get("/operations", response_model=List[OperationResponse])
async def get_operations(status: Optional[str] = None):
    """Get all operations (optionally filtered by status)"""
    # TODO: Fetch from database
    return []

@app.get("/account/balance")
async def get_account_balance():
    """Get current account balance"""
    # TODO: Fetch from OANDA
    return {"balance": 0, "currency": "USD"}

@app.post("/execute/{pair}")
async def execute_trade(pair: str, direction: str, volume: float, stop_loss: float, take_profit: float):
    """Execute a trade manually (for testing)"""
    if direction not in ["BUY", "SELL"]:
        raise HTTPException(status_code=400, detail="Invalid direction")

    # TODO: Execute via OANDA client
    return {"status": "success", "message": f"Order placed for {pair}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
