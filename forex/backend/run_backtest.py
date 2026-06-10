"""
Backtest runner script
Generates synthetic data and runs EMA Crossover strategy backtest
"""

import pandas as pd
import numpy as np
import json
import sys
from datetime import datetime, timedelta
from src.backtest.engine import BacktestEngine
from src.backtest.strategies import get_strategy_config

def generate_realistic_data(pair: str = "EUR_USD", num_days: int = 1260, volatility: float = 0.008):
    """
    Generate realistic OHLC data
    num_days: ~5 years = 1260 trading days
    volatility: daily volatility (0.8% is realistic for forex)
    """
    np.random.seed(42)

    # Base prices for different pairs
    base_prices = {
        'EUR_USD': 1.0800,
        'GBP_USD': 1.2700,
        'USD_JPY': 110.00,
        'USD_CHF': 0.9200,
        'AUD_USD': 0.7400,
    }

    start_price = base_prices.get(pair, 1.0000)
    dates = pd.date_range(end=datetime.now(), periods=num_days, freq='D')

    closes = [start_price]

    # Generate random walk with trend and mean reversion
    trend = 0.0001  # Slight daily uptrend
    mean_reversion = 0.05  # Mean reversion factor

    for i in range(num_days - 1):
        # Random shock
        shock = np.random.randn() * volatility

        # Mean reversion (price tends to return to moving average)
        ma_50 = np.mean(closes[-50:]) if len(closes) >= 50 else closes[-1]
        reversion = mean_reversion * (ma_50 - closes[-1]) / ma_50

        # Next close
        change = trend + shock + reversion
        new_price = closes[-1] * (1 + change)
        closes.append(new_price)

    # Generate OHLC from closes
    data = {
        'Open': [],
        'High': [],
        'Low': [],
        'Close': closes,
    }

    for i, close in enumerate(closes):
        # Random open within day range
        open_price = close * (1 + np.random.randn() * volatility / 3)

        # High and low around close
        high = max(open_price, close) * (1 + abs(np.random.randn()) * volatility / 2)
        low = min(open_price, close) * (1 - abs(np.random.randn()) * volatility / 2)

        data['Open'].append(open_price)
        data['High'].append(high)
        data['Low'].append(low)

    df = pd.DataFrame(data, index=dates)
    return df

def run_single_pair_backtest(pair: str = "EUR_USD", num_days: int = 1260):
    """Run backtest on a single currency pair"""

    print(f"\n{'='*70}")
    print(f"Backtesting {pair} - EMA Crossover Strategy")
    print(f"{'='*70}")

    # Generate data
    print(f"\n1. Generating {num_days} days of synthetic OHLC data...")
    df = generate_realistic_data(pair, num_days)
    print(f"   Date range: {df.index[0].date()} to {df.index[-1].date()}")
    print(f"   Price range: {df['Close'].min():.4f} - {df['Close'].max():.4f}")

    # Run backtest
    print(f"\n2. Running backtest...")
    engine = BacktestEngine(cash=100000, commission=0.0002)
    results = engine.run_backtest(df, pair=pair)

    # Display results
    print(f"\n3. Results:")
    print(f"\n   Performance:")
    print(f"   - Return: {results['return_pct']}")
    print(f"   - Annualized Return: {results['annualized_return']}")
    print(f"   - Sharpe Ratio: {results['sharpe_ratio']}")
    print(f"   - Max Drawdown: {results['max_drawdown']}")

    print(f"\n   Trading Activity:")
    print(f"   - Total Trades: {results['trades']}")
    print(f"   - Wins: {results['wins']}")
    print(f"   - Losses: {results['losses']}")
    print(f"   - Win Rate: {results['win_rate']}")
    print(f"   - Best Trade: {results['best_trade']}")
    print(f"   - Worst Trade: {results['worst_trade']}")
    print(f"   - Avg Trade: {results['avg_trade']}")

    print(f"\n   Final Equity: {results['final_equity']}")

    return results

def run_multi_pair_backtest(pairs: list = None, num_days: int = 1260):
    """Run backtest on multiple currency pairs"""

    if pairs is None:
        pairs = [
            "EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD"
        ]

    all_results = {}

    for pair in pairs:
        try:
            results = run_single_pair_backtest(pair, num_days)
            all_results[pair] = results
        except Exception as e:
            print(f"   ERROR: {e}")
            all_results[pair] = {'error': str(e)}

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY - Multi-Pair Results")
    print(f"{'='*70}\n")

    valid_results = {p: r for p, r in all_results.items() if 'error' not in r}

    if valid_results:
        summary_data = []
        for pair, results in sorted(valid_results.items()):
            summary_data.append({
                'Pair': pair,
                'Return': results['return_pct'],
                'Sharpe': results['sharpe_ratio'],
                'Win Rate': results['win_rate'],
                'Trades': results['trades'],
                'Max DD': results['max_drawdown'],
            })

        summary_df = pd.DataFrame(summary_data)
        print(summary_df.to_string(index=False))

        # Overall stats
        print(f"\nOverall Statistics:")
        print(f"- Avg Sharpe Ratio: {np.nanmean([float(r['sharpe_ratio']) if r['sharpe_ratio'] != 'N/A' else np.nan for r in valid_results.values()]):.2f}")

    return all_results

if __name__ == "__main__":
    # Run backtest
    # Single pair for quick test
    results = run_single_pair_backtest("EUR_USD", num_days=1260)

    # Uncomment for multi-pair
    # results = run_multi_pair_backtest(num_days=1260)

    print(f"\n{'='*70}")
    print("Backtest completed!")
    print(f"{'='*70}\n")
