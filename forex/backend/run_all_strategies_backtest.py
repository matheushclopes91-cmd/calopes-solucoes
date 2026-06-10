"""
Backtest runner for all strategies:
- EMA Crossover (base)
- Larry Williams Setup (EMA 9)
- Palex PC Setup (EMA 21)
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
from src.backtest.engine import BacktestEngine
from src.backtest.strategies import get_strategy_config
from src.analysis.advanced_strategies import (
    LarryWilliamsSetup, PalexPCSetup, HybridMultiStrategyAnalyzer
)

def generate_realistic_data(pair: str = "EUR_USD", num_days: int = 1260, volatility: float = 0.008):
    """Generate realistic OHLC data for backtesting"""
    np.random.seed(42)

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
    trend = 0.0001
    mean_reversion = 0.05

    for i in range(num_days - 1):
        shock = np.random.randn() * volatility
        ma_50 = np.mean(closes[-50:]) if len(closes) >= 50 else closes[-1]
        reversion = mean_reversion * (ma_50 - closes[-1]) / ma_50
        change = trend + shock + reversion
        new_price = closes[-1] * (1 + change)
        closes.append(new_price)

    data = {
        'Open': [],
        'High': [],
        'Low': [],
        'Close': closes,
    }

    for close in closes:
        open_price = close * (1 + np.random.randn() * volatility / 3)
        high = max(open_price, close) * (1 + abs(np.random.randn()) * volatility / 2)
        low = min(open_price, close) * (1 - abs(np.random.randn()) * volatility / 2)
        data['Open'].append(open_price)
        data['High'].append(high)
        data['Low'].append(low)

    df = pd.DataFrame(data, index=dates)
    return df

def test_ema_crossover(pair: str = "EUR_USD", num_days: int = 1260):
    """Test EMA Crossover strategy"""
    print(f"\n{'='*70}")
    print(f"EMA Crossover (50/200) - {pair}")
    print(f"{'='*70}")

    df = generate_realistic_data(pair, num_days)
    print(f"Data: {df.index[0].date()} to {df.index[-1].date()}")

    engine = BacktestEngine(cash=100000, commission=0.0002)
    results = engine.run_backtest(df, pair=pair, strategy_config='moderate')

    print(f"\nResults:")
    print(f"  Return:         {results.get('return_pct', 'N/A')}")
    print(f"  Sharpe Ratio:   {results.get('sharpe_ratio', 'N/A')}")
    print(f"  Win Rate:       {results.get('win_rate', 'N/A')}")
    print(f"  Profit Factor:  {results.get('profit_factor', 'N/A')}")
    print(f"  Max Drawdown:   {results.get('max_drawdown', 'N/A')}")
    print(f"  Total Trades:   {results.get('trades', 'N/A')}")

    return results

def test_larry_williams(pair: str = "EUR_USD", num_days: int = 1260):
    """Test Larry Williams Setup"""
    print(f"\n{'='*70}")
    print(f"Larry Williams Setup (EMA 9 Breakout) - {pair}")
    print(f"{'='*70}")

    df = generate_realistic_data(pair, num_days)
    print(f"Data: {df.index[0].date()} to {df.index[-1].date()}")

    strategy = LarryWilliamsSetup()
    signals, df_analyzed = strategy.analyze(df)

    print(f"\nSignals Generated:")
    print(f"  Total:    {len(signals)}")
    if len(signals) > 0:
        long_count = len(signals[signals['direction'] == 'LONG'])
        short_count = len(signals[signals['direction'] == 'SHORT'])
        print(f"  LONG:     {long_count}")
        print(f"  SHORT:    {short_count}")
        print(f"  Avg Confidence: {signals['confidence'].mean():.2%}")

    results = {
        'strategy': 'LarryWilliams',
        'pair': pair,
        'total_signals': len(signals),
        'long_signals': len(signals[signals['direction'] == 'LONG']) if len(signals) > 0 else 0,
        'short_signals': len(signals[signals['direction'] == 'SHORT']) if len(signals) > 0 else 0,
        'avg_confidence': float(signals['confidence'].mean()) if len(signals) > 0 else 0,
    }

    return results, signals

def test_palex_pc(pair: str = "EUR_USD", num_days: int = 1260):
    """Test Palex PC Setup"""
    print(f"\n{'='*70}")
    print(f"Palex PC Setup (EMA 21 Pullback) - {pair}")
    print(f"{'='*70}")

    df = generate_realistic_data(pair, num_days)
    print(f"Data: {df.index[0].date()} to {df.index[-1].date()}")

    strategy = PalexPCSetup()
    signals, df_analyzed = strategy.analyze(df)

    print(f"\nSignals Generated:")
    print(f"  Total:    {len(signals)}")
    if len(signals) > 0:
        long_count = len(signals[signals['direction'] == 'LONG'])
        short_count = len(signals[signals['direction'] == 'SHORT'])
        print(f"  LONG:     {long_count}")
        print(f"  SHORT:    {short_count}")
        print(f"  Avg Confidence: {signals['confidence'].mean():.2%}")

    results = {
        'strategy': 'PalexPC',
        'pair': pair,
        'total_signals': len(signals),
        'long_signals': len(signals[signals['direction'] == 'LONG']) if len(signals) > 0 else 0,
        'short_signals': len(signals[signals['direction'] == 'SHORT']) if len(signals) > 0 else 0,
        'avg_confidence': float(signals['confidence'].mean()) if len(signals) > 0 else 0,
    }

    return results, signals

def test_hybrid_confluence(pair: str = "EUR_USD", num_days: int = 1260):
    """Test Hybrid Multi-Strategy Analyzer"""
    print(f"\n{'='*70}")
    print(f"Hybrid Multi-Strategy Analyzer (Confluence) - {pair}")
    print(f"{'='*70}")

    df = generate_realistic_data(pair, num_days)
    print(f"Data: {df.index[0].date()} to {df.index[-1].date()}")

    analyzer = HybridMultiStrategyAnalyzer()
    all_signals, confluence_signals, df_analyzed = analyzer.analyze(df)

    print(f"\nAll Signals:")
    print(f"  Total:    {len(all_signals)}")
    if len(all_signals) > 0:
        long_count = len(all_signals[all_signals['direction'] == 'LONG'])
        short_count = len(all_signals[all_signals['direction'] == 'SHORT'])
        print(f"  LONG:     {long_count}")
        print(f"  SHORT:    {short_count}")

    print(f"\n⭐ CONFLUENCE SIGNALS (Higher Probability):")
    print(f"  Total:    {len(confluence_signals)}")
    if len(confluence_signals) > 0:
        long_confluence = len(confluence_signals[confluence_signals['direction'] == 'LONG'])
        short_confluence = len(confluence_signals[confluence_signals['direction'] == 'SHORT'])
        print(f"  LONG:     {long_confluence}")
        print(f"  SHORT:    {short_confluence}")
        print(f"  Avg Confidence: {confluence_signals['confidence'].mean():.2%}")

    results = {
        'strategy': 'HybridConfluence',
        'pair': pair,
        'all_signals': len(all_signals),
        'confluence_signals': len(confluence_signals),
        'confluence_ratio': f"{len(confluence_signals) / len(all_signals) * 100:.1f}%" if len(all_signals) > 0 else "0%",
    }

    return results, all_signals, confluence_signals

def print_comparison_table(all_results):
    """Print comparison table of all strategies"""
    print(f"\n{'='*80}")
    print("COMPARISON TABLE - All Strategies")
    print(f"{'='*80}\n")

    comparison_data = []
    for strategy_name, results in all_results.items():
        row = {
            'Strategy': strategy_name,
        }
        row.update(results)
        comparison_data.append(row)

    comparison_df = pd.DataFrame(comparison_data)
    print(comparison_df.to_string(index=False))

def main():
    print("\n" + "#"*70)
    print("COMPREHENSIVE STRATEGY BACKTEST")
    print("Testing: EMA Crossover + Larry Williams + Palex PC")
    print("#"*70)

    pair = "EUR_USD"
    num_days = 1260  # 5 years

    all_results = {}

    # Test 1: EMA Crossover
    try:
        ema_results = test_ema_crossover(pair, num_days)
        all_results['EMA Crossover'] = ema_results
    except Exception as e:
        print(f"❌ EMA Crossover failed: {e}")

    # Test 2: Larry Williams
    try:
        lw_results, lw_signals = test_larry_williams(pair, num_days)
        all_results['Larry Williams'] = lw_results
    except Exception as e:
        print(f"❌ Larry Williams failed: {e}")

    # Test 3: Palex PC
    try:
        pc_results, pc_signals = test_palex_pc(pair, num_days)
        all_results['Palex PC'] = pc_results
    except Exception as e:
        print(f"❌ Palex PC failed: {e}")

    # Test 4: Hybrid Confluence
    try:
        hybrid_results, all_signals, confluence_signals = test_hybrid_confluence(pair, num_days)
        all_results['Hybrid Confluence'] = hybrid_results
    except Exception as e:
        print(f"❌ Hybrid Confluence failed: {e}")

    # Print comparison
    if all_results:
        print_comparison_table(all_results)

    # Summary
    print(f"\n{'='*80}")
    print("RECOMMENDATIONS")
    print(f"{'='*80}\n")

    if 'Hybrid Confluence' in all_results:
        confluence_ratio = all_results['Hybrid Confluence'].get('confluence_ratio', 'N/A')
        print(f"✅ Confluence Analyzer detected {confluence_ratio} of signals as high-probability")
        print("   → Use confluence-only signals to reduce false positives")

    print(f"\nNext steps:")
    print(f"1. Compare Sharpe ratios across strategies")
    print(f"2. Test on other pairs (GBP/USD, USD/JPY, etc)")
    print(f"3. Run with live data (not synthetic)")
    print(f"4. Paper trade for 2-3 weeks before going live\n")

if __name__ == "__main__":
    main()
