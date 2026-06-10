"""
Weekly trading pipeline:
1. Saturday 14:00 - Run analysis + generate signals
2. Sunday 17:00 - Execute trades
"""

import logging
import pandas as pd
from datetime import datetime
from typing import Dict, List, Any

from src.broker.client import OANDAClient
from src.broker.executor import TradeExecutor
from src.analysis.signals import EMACrossoverStrategy
from src.backtest.strategies import get_strategy_config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class TradingPipeline:
    """Main trading pipeline runner"""

    def __init__(self, strategy_config: str = 'moderate', pairs: List[str] = None):
        """
        Initialize pipeline

        Args:
            strategy_config: 'conservative', 'moderate', 'aggressive', or 'fast'
            pairs: List of currency pairs to trade
        """
        self.client = OANDAClient()
        self.executor = TradeExecutor()
        self.strategy_params = get_strategy_config(strategy_config)
        self.pairs = pairs or OANDAClient.get_major_pairs()

        logger.info(f"TradingPipeline initialized")
        logger.info(f"Strategy: {strategy_config}")
        logger.info(f"Pairs: {', '.join(self.pairs[:5])}... ({len(self.pairs)} total)")

    def analyze_pair(self, pair: str, granularity: str = "D", lookback: int = 500) -> Dict[str, Any]:
        """
        Run analysis on a single pair

        Args:
            pair: Currency pair (e.g., "EUR_USD")
            granularity: Candlestick period (D1 = Daily)
            lookback: Number of candles to fetch

        Returns:
            Analysis result with signals
        """
        logger.info(f"\nAnalyzing {pair}...")

        # Fetch quotes
        df = self.client.get_quotes(pair, granularity=granularity, count=lookback)
        if df is None or len(df) < self.strategy_params.ema_slow:
            logger.warning(f"  ⚠️  Insufficient data for {pair}")
            return {'pair': pair, 'status': 'skipped', 'reason': 'Insufficient data'}

        # Run strategy
        strategy = EMACrossoverStrategy(risk_percentage=self.strategy_params.risk_percentage)
        signals, analyzed_df = strategy.analyze(df)

        logger.info(f"  Found {len(signals)} signals")

        result = {
            'pair': pair,
            'status': 'success',
            'signals': signals.to_dict('records') if len(signals) > 0 else [],
            'last_price': df['close'].iloc[-1],
            'analyzed_df': analyzed_df
        }

        return result

    def run_analysis(self) -> Dict[str, Any]:
        """
        Run analysis on all pairs (Saturday 14:00)

        Returns:
            Analysis results for all pairs
        """
        logger.info("\n" + "="*70)
        logger.info("WEEKLY ANALYSIS - Saturday 14:00")
        logger.info("="*70)

        all_results = {}
        all_signals = []

        for pair in self.pairs:
            try:
                result = self.analyze_pair(pair)
                all_results[pair] = result

                if result['status'] == 'success' and len(result['signals']) > 0:
                    for signal in result['signals']:
                        signal['pair'] = pair
                        all_signals.append(signal)

            except Exception as e:
                logger.error(f"Error analyzing {pair}: {e}")
                all_results[pair] = {'pair': pair, 'status': 'error', 'error': str(e)}

        logger.info(f"\n{'='*70}")
        logger.info(f"Analysis complete - {len(all_signals)} signals generated")
        logger.info(f"{'='*70}")

        return {
            'timestamp': datetime.now().isoformat(),
            'pairs_analyzed': len(self.pairs),
            'total_signals': len(all_signals),
            'signals': all_signals,
            'pair_results': all_results
        }

    def execute_signals(self, signals: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Execute trades based on signals (Sunday 17:00)

        Args:
            signals: List of signals from analysis

        Returns:
            Execution results
        """
        logger.info("\n" + "="*70)
        logger.info("TRADE EXECUTION - Sunday 17:00")
        logger.info(f"Executing {len(signals)} signals")
        logger.info("="*70)

        execution_results = []

        for signal in signals:
            pair = signal['pair']
            direction = signal['direction']
            entry_price = signal['entry_price']
            stop_loss = signal['stop_loss']
            take_profit = signal['take_profit']

            try:
                # Check if already have open position on this pair
                open_positions = self.executor.get_open_positions()
                if any(p['pair'] == pair for p in open_positions):
                    logger.warning(f"Skipping {pair} - Already have open position")
                    continue

                # Execute
                result = self.executor.execute_signal(
                    {
                        'direction': direction,
                        'entry_price': entry_price,
                        'stop_loss': stop_loss,
                        'take_profit': take_profit,
                        'confidence': signal.get('confidence', 0.5)
                    },
                    pair
                )

                execution_results.append(result)

            except Exception as e:
                logger.error(f"Error executing {pair}: {e}")
                execution_results.append({
                    'status': 'error',
                    'pair': pair,
                    'error': str(e)
                })

        successful = sum(1 for r in execution_results if r['status'] == 'success')
        logger.info(f"\n{'='*70}")
        logger.info(f"Execution complete - {successful}/{len(signals)} trades executed")
        logger.info(f"{'='*70}\n")

        return {
            'timestamp': datetime.now().isoformat(),
            'signals_count': len(signals),
            'executed_count': successful,
            'results': execution_results
        }

    def run_weekly_cycle(self):
        """
        Run complete weekly cycle:
        1. Saturday 14:00 - Analysis
        2. Sunday 17:00 - Execution
        """
        logger.info(f"\n{'#'*70}")
        logger.info(f"WEEKLY TRADING CYCLE - {datetime.now()}")
        logger.info(f"{'#'*70}\n")

        # Step 1: Analysis
        analysis_results = self.run_analysis()

        # Step 2: Execution (if signals generated)
        if len(analysis_results['signals']) > 0:
            execution_results = self.execute_signals(analysis_results['signals'])
            logger.info(f"\nExecution Summary:")
            logger.info(f"- Signals: {execution_results['signals_count']}")
            logger.info(f"- Executed: {execution_results['executed_count']}")
        else:
            logger.info("\nNo signals generated, skipping execution")
            execution_results = None

        return {
            'analysis': analysis_results,
            'execution': execution_results,
            'timestamp': datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Run pipeline manually (for testing)
    pipeline = TradingPipeline(strategy_config='moderate')

    # Only run on analysis phase (don't execute trades)
    results = pipeline.run_analysis()

    print("\n" + "="*70)
    print("Summary:")
    print(f"- Pairs analyzed: {results['pairs_analyzed']}")
    print(f"- Total signals: {results['total_signals']}")
    print("="*70)

    # To execute trades, uncomment:
    # execution = pipeline.execute_signals(results['signals'])
