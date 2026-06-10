"""
Test script to validate EMA Crossover Strategy with sample data
"""

import pandas as pd
import numpy as np
from src.analysis.signals import EMACrossoverStrategy

def generate_sample_data(num_candles=500):
    """Generate synthetic OHLC data for testing"""
    np.random.seed(42)

    # Start with base price
    prices = [1.0800]

    # Generate random walk
    for _ in range(num_candles - 1):
        change = np.random.randn() * 0.001  # ~0.1% daily volatility
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

def test_ema_crossover_strategy():
    """Test EMA Crossover strategy with synthetic data"""

    print("=" * 60)
    print("EMA Crossover Strategy Test")
    print("=" * 60)

    # Generate test data
    print("\n1. Generating synthetic OHLC data (500 days)...")
    df = generate_sample_data(500)
    print(f"   Data shape: {df.shape}")
    print(f"   Date range: {df.index[0].date()} to {df.index[-1].date()}")
    print(f"   Price range: {df['close'].min():.4f} - {df['close'].max():.4f}")

    # Initialize strategy
    print("\n2. Initializing EMA Crossover Strategy...")
    strategy = EMACrossoverStrategy(risk_percentage=0.8)
    print(f"   EMA Fast: {strategy.ema_fast}")
    print(f"   EMA Slow: {strategy.ema_slow}")
    print(f"   RSI Period: {strategy.rsi_period}")
    print(f"   Risk per trade: {strategy.risk_percentage}%")

    # Run analysis
    print("\n3. Running analysis...")
    signals, analyzed_df = strategy.analyze(df)

    # Display results
    print(f"\n4. Results:")
    print(f"   Total signals generated: {len(signals)}")

    if len(signals) > 0:
        long_signals = len(signals[signals['direction'] == 'LONG'])
        short_signals = len(signals[signals['direction'] == 'SHORT'])
        print(f"   LONG signals: {long_signals}")
        print(f"   SHORT signals: {short_signals}")

        print(f"\n5. Latest 5 Signals:")
        print(signals.tail(5).to_string())

        # Calculate some stats
        avg_confidence = signals['confidence'].mean()
        print(f"\n6. Statistics:")
        print(f"   Average confidence: {avg_confidence:.2%}")
        print(f"   Min confidence: {signals['confidence'].min():.2%}")
        print(f"   Max confidence: {signals['confidence'].max():.2%}")

        # Display last analyzed data with indicators
        print(f"\n7. Last Candle Analysis:")
        last_row = analyzed_df.iloc[-1]
        print(f"   Close: {last_row['close']:.4f}")
        print(f"   EMA50: {last_row['ema50']:.4f}")
        print(f"   EMA200: {last_row['ema200']:.4f}")
        print(f"   RSI: {last_row['rsi']:.2f}")
        print(f"   ATR: {last_row['atr']:.4f}")

        if last_row['ema50'] > last_row['ema200']:
            print(f"   Trend: UPTREND (EMA50 > EMA200)")
        else:
            print(f"   Trend: DOWNTREND (EMA50 < EMA200)")
    else:
        print("   No signals generated (insufficient data or no crossovers)")

    print("\n" + "=" * 60)
    print("Test completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    test_ema_crossover_strategy()
