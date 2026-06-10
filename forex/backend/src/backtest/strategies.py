from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class EMACrossoverParams:
    """Parameters for EMA Crossover strategy"""
    ema_fast: int = 50
    ema_slow: int = 200
    rsi_period: int = 14
    rsi_overbought: int = 70
    rsi_oversold: int = 30
    atr_multiplier: float = 2.0
    rr_ratio: float = 2.0  # Risk-Reward ratio
    risk_percentage: float = 0.8  # % of equity per trade

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'ema_fast': self.ema_fast,
            'ema_slow': self.ema_slow,
            'rsi_period': self.rsi_period,
            'rsi_overbought': self.rsi_overbought,
            'rsi_oversold': self.rsi_oversold,
            'atr_multiplier': self.atr_multiplier,
            'rr_ratio': self.rr_ratio,
            'risk_percentage': self.risk_percentage,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EMACrossoverParams':
        """Create from dictionary"""
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


# Predefined strategy configurations
STRATEGY_CONFIGS = {
    'conservative': EMACrossoverParams(
        ema_fast=50,
        ema_slow=200,
        rsi_period=14,
        rsi_overbought=70,
        rsi_oversold=30,
        atr_multiplier=3.0,  # Wider stops
        rr_ratio=2.5,
        risk_percentage=0.5,  # Lower risk
    ),
    'moderate': EMACrossoverParams(
        ema_fast=50,
        ema_slow=200,
        rsi_period=14,
        rsi_overbought=70,
        rsi_oversold=30,
        atr_multiplier=2.0,  # Standard
        rr_ratio=2.0,
        risk_percentage=0.8,  # Medium risk
    ),
    'aggressive': EMACrossoverParams(
        ema_fast=50,
        ema_slow=200,
        rsi_period=14,
        rsi_overbought=65,  # More sensitive
        rsi_oversold=35,
        atr_multiplier=1.5,  # Tighter stops
        rr_ratio=1.5,
        risk_percentage=1.0,  # Higher risk
    ),
    'fast': EMACrossoverParams(
        ema_fast=20,
        ema_slow=50,
        rsi_period=9,
        rsi_overbought=70,
        rsi_oversold=30,
        atr_multiplier=1.5,
        rr_ratio=1.5,
        risk_percentage=0.6,
    ),
}


def get_strategy_config(name: str = 'moderate') -> EMACrossoverParams:
    """Get predefined strategy configuration"""
    if name not in STRATEGY_CONFIGS:
        raise ValueError(f"Unknown strategy: {name}. Available: {list(STRATEGY_CONFIGS.keys())}")
    return STRATEGY_CONFIGS[name]
