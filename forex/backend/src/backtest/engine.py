import pandas as pd
import numpy as np
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import json
from datetime import datetime
from typing import Dict, Any

class EMACrossoverBacktest(Strategy):
    """EMA Crossover strategy for backtesting"""

    # Define parameters
    ema_fast = 50
    ema_slow = 200
    rsi_period = 14
    rsi_overbought = 70
    rsi_oversold = 30
    atr_multiplier = 2
    rr_ratio = 2
    risk_percentage = 0.8

    def init(self):
        """Initialize indicators"""
        # EMA indicators
        self.ema_fast_line = self.I(lambda x: pd.Series(x).ewm(span=self.ema_fast, adjust=False).mean())
        self.ema_slow_line = self.I(lambda x: pd.Series(x).ewm(span=self.ema_slow, adjust=False).mean())

        # RSI
        self.rsi = self.I(self._rsi, self.data.Close, self.rsi_period)

        # ATR
        self.atr = self.I(self._atr, self.data.High, self.data.Low, self.data.Close, 14)

    def next(self):
        """Execute strategy logic on each bar"""
        if len(self.data) < self.ema_slow:
            return

        # Skip if missing values
        if np.isnan(self.ema_fast_line[-1]) or np.isnan(self.ema_slow_line[-1]) or np.isnan(self.atr[-1]):
            return

        current_price = self.data.Close[-1]
        atr_value = self.atr[-1]

        # Bullish crossover (EMA50 crosses above EMA200) + RSI confirmation
        if (self.ema_fast_line[-1] > self.ema_slow_line[-1] and
            self.ema_fast_line[-2] <= self.ema_slow_line[-2] and
            self.rsi[-1] < self.rsi_overbought and
            not self.position):

            # Calculate position size based on risk
            stop_loss = current_price - (atr_value * self.atr_multiplier)
            risk_amount = current_price - stop_loss
            position_size = (self.equity * self.risk_percentage / 100) / risk_amount if risk_amount > 0 else 0

            if position_size > 0:
                take_profit = current_price + (risk_amount * self.rr_ratio)
                self.buy(size=position_size, tp=take_profit, sl=stop_loss)

        # Bearish crossover (EMA50 crosses below EMA200) + RSI confirmation
        elif (self.ema_fast_line[-1] < self.ema_slow_line[-1] and
              self.ema_fast_line[-2] >= self.ema_slow_line[-2] and
              self.rsi[-1] > self.rsi_oversold and
              self.position):

            self.position.close()

    @staticmethod
    def _rsi(data, period=14):
        """Calculate RSI"""
        delta = pd.Series(data).diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi.values

    @staticmethod
    def _atr(high, low, close, period=14):
        """Calculate ATR"""
        high = pd.Series(high)
        low = pd.Series(low)
        close = pd.Series(close)

        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())

        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()
        return atr.values


class BacktestEngine:
    """Backtesting engine for forex strategies"""

    def __init__(self, cash=100000, commission=0.0002):
        self.cash = cash
        self.commission = commission

    def run_backtest(self, df: pd.DataFrame, pair: str = "EUR_USD") -> Dict[str, Any]:
        """
        Run backtest on OHLC data

        Args:
            df: DataFrame with columns [Open, High, Low, Close, Volume]
            pair: Currency pair name

        Returns:
            Dictionary with backtest results
        """
        # Ensure DataFrame has correct column names
        df = df.copy()
        if not all(col in df.columns for col in ['Open', 'High', 'Low', 'Close']):
            # Try to rename if columns are lowercase
            df.columns = [col.capitalize() if col.lower() in ['open', 'high', 'low', 'close', 'volume'] else col
                         for col in df.columns]

        # Ensure index is datetime
        if not isinstance(df.index, pd.DatetimeIndex):
            if 'Date' in df.columns or 'Datetime' in df.columns:
                date_col = 'Date' if 'Date' in df.columns else 'Datetime'
                df.index = pd.to_datetime(df[date_col])
                df = df.drop(columns=[date_col])
            else:
                df.index = pd.to_datetime(df.index)

        # Run backtest
        bt = Backtest(df, EMACrossoverBacktest, cash=self.cash, commission=self.commission)
        stats = bt.run()

        # Extract results
        results = {
            'pair': pair,
            'start_date': str(df.index[0].date()),
            'end_date': str(df.index[-1].date()),
            'total_days': len(df),

            # Performance metrics
            'start': stats['Start'],
            'end': stats['End'],
            'duration': str(stats['Duration']),
            'exposure_time': f"{stats['Exposure Time']:.2%}",

            # Returns
            'return_pct': f"{stats['Return [%]']:.2f}%",
            'annualized_return': f"{stats['Return (Ann.) [%]']:.2f}%",
            'buy_hold_return': f"{stats['Buy & Hold Return [%]']:.2f}%",

            # Risk metrics
            'sharpe_ratio': f"{stats.get('Sharpe Ratio', 'N/A')}",
            'max_drawdown': f"{stats['Max. Drawdown [%]']:.2f}%",
            'sortino_ratio': f"{stats.get('Sortino Ratio', 'N/A')}",

            # Trade statistics
            'trades': int(stats['# Trades']),
            'wins': int(stats['Win Rate [%]'] * stats['# Trades'] / 100) if stats['# Trades'] > 0 else 0,
            'losses': int(stats['# Trades'] - (stats['Win Rate [%]'] * stats['# Trades'] / 100)) if stats['# Trades'] > 0 else 0,
            'win_rate': f"{stats['Win Rate [%]']:.2f}%",
            'best_trade': f"{stats['Best Trade [%]']:.2f}%",
            'worst_trade': f"{stats['Worst Trade [%]']:.2f}%",
            'avg_trade': f"{stats['Avg. Trade [%]']:.2f}%",

            # Profit/Loss
            'profit_factor': f"{stats.get('Profit Factor', 'N/A')}",
            'expectancy': f"{stats.get('Expectancy [%]', 'N/A')}",

            # Summary
            'final_equity': f"${stats['_equity_final']:.2f}",
            'raw_stats': {
                'Return [%]': stats['Return [%]'],
                'Win Rate [%]': stats['Win Rate [%]'],
                'Max. Drawdown [%]': stats['Max. Drawdown [%]'],
                '# Trades': stats['# Trades'],
            }
        }

        return results

    def run_walk_forward(self, df: pd.DataFrame, pair: str = "EUR_USD",
                        train_window: int = 252, test_window: int = 63) -> Dict[str, Any]:
        """
        Run walk-forward analysis (train-test splits)

        Args:
            df: Full OHLC data
            pair: Currency pair name
            train_window: Training period in days
            test_window: Testing period in days

        Returns:
            Dictionary with walk-forward results
        """
        results = {
            'pair': pair,
            'train_window': train_window,
            'test_window': test_window,
            'windows': []
        }

        total_len = len(df)
        position = 0

        while position + train_window + test_window <= total_len:
            train_end = position + train_window
            test_end = train_end + test_window

            # Train period
            train_data = df.iloc[position:train_end]

            # Test period
            test_data = df.iloc[train_end:test_end]

            # Run test
            test_results = self.run_backtest(test_data, pair)

            results['windows'].append({
                'train_period': f"{train_data.index[0].date()} to {train_data.index[-1].date()}",
                'test_period': f"{test_data.index[0].date()} to {test_data.index[-1].date()}",
                'test_results': test_results
            })

            position = train_end

        # Summary
        if results['windows']:
            avg_sharpe = np.nanmean([
                float(w['test_results']['sharpe_ratio']) if w['test_results']['sharpe_ratio'] != 'N/A' else np.nan
                for w in results['windows']
            ])
            avg_win_rate = np.nanmean([
                float(w['test_results']['win_rate'].rstrip('%')) / 100
                for w in results['windows']
            ])

            results['summary'] = {
                'total_windows': len(results['windows']),
                'avg_sharpe_ratio': f"{avg_sharpe:.2f}" if not np.isnan(avg_sharpe) else "N/A",
                'avg_win_rate': f"{avg_win_rate:.2%}",
            }

        return results
