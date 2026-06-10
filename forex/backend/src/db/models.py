from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    pair = Column(String(10), index=True)
    timestamp = Column(DateTime, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

    __table_args__ = ({"indexes": [("pair", "timestamp")]},)

class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True)
    pair = Column(String(10), index=True)
    timestamp = Column(DateTime, index=True)
    direction = Column(String(5))  # LONG or SHORT
    entry_price = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    risk_percentage = Column(Float)
    confidence = Column(Float)  # 0-1

class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True)
    pair = Column(String(10))
    direction = Column(String(5))  # LONG or SHORT
    entry_price = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    entry_time = Column(DateTime)
    exit_time = Column(DateTime, nullable=True)
    exit_price = Column(Float, nullable=True)
    pnl = Column(Float, nullable=True)
    status = Column(String(20))  # OPEN, CLOSED, CANCELLED
    volume = Column(Float)
