import pandas as pd
import numpy as np
from .indicators import ema, rsi, atr

class EMACrossoverStrategy:
    """
    EMA 50/200 Crossover Strategy
    - LONG: EMA50 crosses above EMA200 + RSI < 70
    - SHORT: EMA50 crosses below EMA200 + RSI > 30
    - Stop Loss: ATR × 2
    - Take Profit: RRR 1:2
    """

    def __init__(self, risk_percentage=0.8):
        self.ema_fast = 50
        self.ema_slow = 200
        self.rsi_period = 14
        self.rsi_overbought = 70
        self.rsi_oversold = 30
        self.atr_multiplier = 2
        self.rr_ratio = 2  # 1:2 risk-reward
        self.risk_percentage = risk_percentage

    def analyze(self, df):
        """
        Analyze OHLC data and return signals
        df: DataFrame with columns [open, high, low, close, volume]
        """
        df = df.copy()
        df['ema50'] = ema(df['close'], self.ema_fast)
        df['ema200'] = ema(df['close'], self.ema_slow)
        df['rsi'] = rsi(df['close'], self.rsi_period)
        df['atr'] = atr(df['high'], df['low'], df['close'])

        # Detect crossovers
        df['ema_cross'] = 0
        df.loc[
            (df['ema50'] > df['ema200']) &
            (df['ema50'].shift(1) <= df['ema200'].shift(1)),
            'ema_cross'
        ] = 1  # Bullish crossover
        df.loc[
            (df['ema50'] < df['ema200']) &
            (df['ema50'].shift(1) >= df['ema200'].shift(1)),
            'ema_cross'
        ] = -1  # Bearish crossover

        # Generate signals
        signals = []
        for idx, row in df.iterrows():
            if pd.isna(row['atr']) or pd.isna(row['rsi']):
                continue

            if row['ema_cross'] == 1 and row['rsi'] < self.rsi_overbought:
                # LONG signal
                stop_loss = row['close'] - (row['atr'] * self.atr_multiplier)
                risk = row['close'] - stop_loss
                take_profit = row['close'] + (risk * self.rr_ratio)

                signals.append({
                    'timestamp': row.name if isinstance(row.name, pd.Timestamp) else idx,
                    'direction': 'LONG',
                    'entry_price': row['close'],
                    'stop_loss': stop_loss,
                    'take_profit': take_profit,
                    'risk': risk,
                    'confidence': min(1.0, (100 - row['rsi']) / 100)
                })

            elif row['ema_cross'] == -1 and row['rsi'] > self.rsi_oversold:
                # SHORT signal
                stop_loss = row['close'] + (row['atr'] * self.atr_multiplier)
                risk = stop_loss - row['close']
                take_profit = row['close'] - (risk * self.rr_ratio)

                signals.append({
                    'timestamp': row.name if isinstance(row.name, pd.Timestamp) else idx,
                    'direction': 'SHORT',
                    'entry_price': row['close'],
                    'stop_loss': stop_loss,
                    'take_profit': take_profit,
                    'risk': risk,
                    'confidence': min(1.0, row['rsi'] / 100)
                })

        return pd.DataFrame(signals), df
