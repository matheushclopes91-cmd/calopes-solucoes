"""
Advanced trading strategies:
- Larry Williams Setup (EMA 9)
- Palex PC Setup (EMA 21)
"""

import pandas as pd
import numpy as np
from .indicators import ema, rsi, atr


class LarryWilliamsSetup:
    """
    Larry Williams Strategy - Breakout on 5-day high/low

    Rules:
    - EMA 9 as trend confirmation
    - Break above 5-day high = LONG (if EMA9 > EMA20)
    - Break below 5-day low = SHORT (if EMA9 < EMA20)
    - ATR-based stops
    - RRR 1:2
    """

    def __init__(self, lookback_period: int = 5, atr_multiplier: float = 2.0, risk_percentage: float = 0.8):
        self.lookback_period = lookback_period  # 5-day high/low
        self.ema_fast = 9
        self.ema_slow = 20
        self.atr_multiplier = atr_multiplier
        self.rr_ratio = 2.0
        self.risk_percentage = risk_percentage

    def analyze(self, df: pd.DataFrame):
        """
        Analyze OHLC data for Larry Williams setups
        """
        df = df.copy()

        # Indicators
        df['ema9'] = ema(df['close'], self.ema_fast)
        df['ema20'] = ema(df['close'], self.ema_slow)
        df['atr'] = atr(df['high'], df['low'], df['close'])

        # 5-day highs and lows
        df['high_5d'] = df['high'].rolling(window=self.lookback_period).max()
        df['low_5d'] = df['low'].rolling(window=self.lookback_period).min()

        signals = []

        for idx in range(self.lookback_period, len(df)):
            current = df.iloc[idx]
            prev = df.iloc[idx - 1]

            if pd.isna(current['atr']) or pd.isna(current['ema9']):
                continue

            # LONG: Break above 5-day high + EMA9 > EMA20
            if (current['high'] > current['high_5d'] and
                prev['high'] <= prev['high_5d'] and
                current['ema9'] > current['ema20']):

                entry = current['high']
                stop_loss = current['low'] - (current['atr'] * self.atr_multiplier)
                risk = entry - stop_loss
                take_profit = entry + (risk * self.rr_ratio)

                signals.append({
                    'timestamp': idx,
                    'direction': 'LONG',
                    'entry_price': entry,
                    'stop_loss': stop_loss,
                    'take_profit': take_profit,
                    'risk': risk,
                    'confidence': 0.75
                })

            # SHORT: Break below 5-day low + EMA9 < EMA20
            elif (current['low'] < current['low_5d'] and
                  prev['low'] >= prev['low_5d'] and
                  current['ema9'] < current['ema20']):

                entry = current['low']
                stop_loss = current['high'] + (current['atr'] * self.atr_multiplier)
                risk = stop_loss - entry
                take_profit = entry - (risk * self.rr_ratio)

                signals.append({
                    'timestamp': idx,
                    'direction': 'SHORT',
                    'entry_price': entry,
                    'stop_loss': stop_loss,
                    'take_profit': take_profit,
                    'risk': risk,
                    'confidence': 0.75
                })

        return pd.DataFrame(signals), df


class PalexPCSetup:
    """
    Palex PC Setup - Pullback on EMA 21

    Rules:
    - EMA 21 as support/resistance
    - Price pulls back to EMA21 after trending move
    - Enter on touch of EMA21 with confirmation
    - Stop below the pullback candle
    - RRR 1:2.5
    """

    def __init__(self, ema_period: int = 21, pullback_threshold: float = 0.005, risk_percentage: float = 0.8):
        self.ema_period = ema_period  # EMA 21
        self.pullback_threshold = pullback_threshold  # 0.5% threshold
        self.atr_multiplier = 1.5
        self.rr_ratio = 2.5
        self.risk_percentage = risk_percentage

    def analyze(self, df: pd.DataFrame):
        """
        Analyze OHLC data for Palex PC setups
        """
        df = df.copy()

        # Indicators
        df['ema21'] = ema(df['close'], self.ema_period)
        df['atr'] = atr(df['high'], df['low'], df['close'])

        # Distance from EMA21
        df['distance_from_ema'] = abs(df['close'] - df['ema21']) / df['close']

        signals = []
        trend_state = {}  # Track trend direction per session

        for idx in range(self.ema_period + 1, len(df)):
            current = df.iloc[idx]
            prev = df.iloc[idx - 1]

            if pd.isna(current['atr']) or pd.isna(current['ema21']):
                continue

            # Detect uptrend: price clearly above EMA21
            if current['close'] > current['ema21'] * (1 + self.pullback_threshold):
                trend_state['direction'] = 'up'
                trend_state['entry_level'] = max(trend_state.get('entry_level', 0), current['high'])

            # Detect downtrend: price clearly below EMA21
            elif current['close'] < current['ema21'] * (1 - self.pullback_threshold):
                trend_state['direction'] = 'down'
                trend_state['entry_level'] = min(trend_state.get('entry_level', float('inf')), current['low'])

            # Pullback setup: price touches/pulls back to EMA21

            # LONG: Uptrend + Price touches EMA21 from above
            if (trend_state.get('direction') == 'up' and
                current['distance_from_ema'] < self.pullback_threshold and
                prev['distance_from_ema'] >= self.pullback_threshold and
                current['close'] > current['ema21']):

                entry = current['close']
                stop_loss = prev['low'] - (current['atr'] * self.atr_multiplier)
                risk = entry - stop_loss
                take_profit = entry + (risk * self.rr_ratio)

                signals.append({
                    'timestamp': idx,
                    'direction': 'LONG',
                    'entry_price': entry,
                    'stop_loss': stop_loss,
                    'take_profit': take_profit,
                    'risk': risk,
                    'confidence': 0.80
                })

            # SHORT: Downtrend + Price touches EMA21 from below
            elif (trend_state.get('direction') == 'down' and
                  current['distance_from_ema'] < self.pullback_threshold and
                  prev['distance_from_ema'] >= self.pullback_threshold and
                  current['close'] < current['ema21']):

                entry = current['close']
                stop_loss = prev['high'] + (current['atr'] * self.atr_multiplier)
                risk = stop_loss - entry
                take_profit = entry - (risk * self.rr_ratio)

                signals.append({
                    'timestamp': idx,
                    'direction': 'SHORT',
                    'entry_price': entry,
                    'stop_loss': stop_loss,
                    'take_profit': take_profit,
                    'risk': risk,
                    'confidence': 0.80
                })

        return pd.DataFrame(signals), df


class HybridMultiStrategyAnalyzer:
    """
    Combines EMA Crossover, Larry Williams, and Palex PC setups
    Uses confluence of signals for higher probability entries
    """

    def __init__(self):
        self.ema_crossover = None  # Will be set later
        self.larry_williams = LarryWilliamsSetup()
        self.palex_pc = PalexPCSetup()

    def analyze(self, df: pd.DataFrame):
        """
        Run all strategies and identify confluence signals
        """
        df = df.copy()

        # Run each strategy
        lw_signals, df_lw = self.larry_williams.analyze(df)
        pc_signals, df_pc = self.palex_pc.analyze(df)

        # Mark signals by strategy
        lw_signals['strategy'] = 'LarryWilliams'
        pc_signals['strategy'] = 'PalexPC'

        # Combine signals
        all_signals = pd.concat([lw_signals, pc_signals], ignore_index=True)
        all_signals = all_signals.sort_values('timestamp').reset_index(drop=True)

        # Identify confluence (same direction signals close together)
        confluence_signals = self._find_confluence(all_signals)

        return all_signals, confluence_signals, df

    def _find_confluence(self, signals: pd.DataFrame, window: int = 2) -> pd.DataFrame:
        """
        Find signals that confirm each other (confluence)
        Two signals of same direction within 'window' candles = higher confidence
        """
        if len(signals) < 2:
            return pd.DataFrame()

        confluence = []

        for i in range(len(signals)):
            current = signals.iloc[i]

            # Look for same direction signals within window
            matching = signals[
                (signals['direction'] == current['direction']) &
                (abs(signals['timestamp'] - current['timestamp']) <= window) &
                (signals['strategy'] != current['strategy'])
            ]

            if len(matching) > 0:
                # Confluence signal found
                confluence_signal = current.copy()
                confluence_signal['confluence'] = True
                confluence_signal['confirming_strategies'] = matching['strategy'].tolist()
                confluence_signal['confidence'] = min(1.0, current['confidence'] * 1.2)  # Boost confidence
                confluence.append(confluence_signal)

        return pd.DataFrame(confluence) if confluence else pd.DataFrame()
