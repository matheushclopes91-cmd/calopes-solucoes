"""
Test script for advanced strategies:
- Larry Williams Setup (EMA 9)
- Palex PC Setup (EMA 21)
- Hybrid confluence analyzer
"""

import pandas as pd
import numpy as np
from src.analysis.advanced_strategies import (
    LarryWilliamsSetup, PalexPCSetup, HybridMultiStrategyAnalyzer
)

def generate_sample_data(num_candles=500):
    """Generate synthetic OHLC data for testing"""
    np.random.seed(42)

    prices = [1.0800]
    for _ in range(num_candles - 1):
        change = np.random.randn() * 0.001
        prices.append(prices[-1] * (1 + change))

    dates = pd.date_range('2024-01-01', periods=num_candles, freq='D')

    data = {
        'timestamp': dates,
        'close': prices,
        'open': [p * (1 + np.random.randn() * 0.0005) for p in prices],
        'high': [p * (1 + abs(np.random.randn()) * 0.001) for p in prices],
        'low': [p * (1 - abs(np.random.randn()) * 0.001) for p in prices],
        'volume': np.random.randint(1000, 5000, num_candles)
    }

    df = pd.DataFrame(data)
    df.set_index('timestamp', inplace=True)
    return df

def test_larry_williams():
    """Test Larry Williams setup"""
    print("\n" + "="*70)
    print("Larry Williams Setup (EMA 9 Breakout)")
    print("="*70)

    df = generate_sample_data(500)

    strategy = LarryWilliamsSetup()
    signals, analyzed_df = strategy.analyze(df)

    print(f"\nTotal signals: {len(signals)}")
    if len(signals) > 0:
        long_signals = len(signals[signals['direction'] == 'LONG'])
        short_signals = len(signals[signals['direction'] == 'SHORT'])
        print(f"LONG signals: {long_signals}")
        print(f"SHORT signals: {short_signals}")
        print(f"\nLatest 3 signals:")
        print(signals.tail(3).to_string())

def test_palex_pc():
    """Test Palex PC setup"""
    print("\n" + "="*70)
    print("Palex PC Setup (EMA 21 Pullback)")
    print("="*70)

    df = generate_sample_data(500)

    strategy = PalexPCSetup()
    signals, analyzed_df = strategy.analyze(df)

    print(f"\nTotal signals: {len(signals)}")
    if len(signals) > 0:
        long_signals = len(signals[signals['direction'] == 'LONG'])
        short_signals = len(signals[signals['direction'] == 'SHORT'])
        print(f"LONG signals: {long_signals}")
        print(f"SHORT signals: {short_signals}")
        print(f"\nLatest 3 signals:")
        print(signals.tail(3).to_string())

def test_hybrid_confluence():
    """Test hybrid multi-strategy confluence"""
    print("\n" + "="*70)
    print("Hybrid Multi-Strategy Analyzer (Confluence)")
    print("="*70)

    df = generate_sample_data(500)

    analyzer = HybridMultiStrategyAnalyzer()
    all_signals, confluence_signals, analyzed_df = analyzer.analyze(df)

    print(f"\nTotal signals from all strategies: {len(all_signals)}")
    print(f"Larry Williams signals: {len(all_signals[all_signals['strategy'] == 'LarryWilliams'])}")
    print(f"Palex PC signals: {len(all_signals[all_signals['strategy'] == 'PalexPC'])}")

    print(f"\n⭐ CONFLUENCE SIGNALS (Higher probability): {len(confluence_signals)}")
    if len(confluence_signals) > 0:
        print("\nConfluence signals (multiple strategies confirm):")
        for idx, sig in confluence_signals.iterrows():
            print(f"  - {sig['direction']} @ {sig['entry_price']:.5f}")
            print(f"    Confirming: {', '.join(sig['confirming_strategies'])}")
            print(f"    Confidence: {sig['confidence']:.0%}\n")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("Advanced Strategies Test")
    print("#"*70)

    test_larry_williams()
    test_palex_pc()
    test_hybrid_confluence()

    print("\n" + "#"*70)
    print("Test completed!")
    print("#"*70 + "\n")
