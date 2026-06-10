from datetime import datetime
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .runner import TradingPipeline

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ForexScheduler:
    """Manages scheduled analysis and execution tasks"""

    def __init__(self, strategy_config: str = 'moderate'):
        self.scheduler = BackgroundScheduler()
        self.pipeline = TradingPipeline(strategy_config=strategy_config)
        self.latest_signals = None

    def start(self):
        """Start the scheduler"""
        # Saturday 14:00 (2 PM) - Run analysis + generate signals
        self.scheduler.add_job(
            self.run_analysis,
            trigger=CronTrigger(day_of_week=5, hour=14, minute=0),  # Saturday
            id='weekly_analysis',
            name='Weekly Analysis'
        )

        # Sunday 17:00 (5 PM) - Execute trades (1 hour before market open)
        self.scheduler.add_job(
            self.execute_trades,
            trigger=CronTrigger(day_of_week=6, hour=17, minute=0),  # Sunday
            id='execute_trades',
            name='Execute Trades'
        )

        self.scheduler.start()
        logger.info("✅ Scheduler started")
        logger.info(f"  - Saturday 14:00: Analysis")
        logger.info(f"  - Sunday 17:00: Execution")

    def run_analysis(self):
        """Run weekly analysis + backtesting"""
        logger.info(f"\n{'='*70}")
        logger.info(f"SCHEDULED TASK: Weekly Analysis")
        logger.info(f"{'='*70}")

        try:
            results = self.pipeline.run_analysis()
            self.latest_signals = results['signals']

            logger.info(f"✅ Analysis complete - {results['total_signals']} signals generated")
            return results

        except Exception as e:
            logger.error(f"❌ Analysis failed: {e}")
            return None

    def execute_trades(self):
        """Execute trades based on latest signals"""
        logger.info(f"\n{'='*70}")
        logger.info(f"SCHEDULED TASK: Trade Execution")
        logger.info(f"{'='*70}")

        if not self.latest_signals:
            logger.warning("No signals available for execution")
            return None

        try:
            results = self.pipeline.execute_signals(self.latest_signals)
            logger.info(f"✅ Execution complete - {results['executed_count']} trades executed")
            return results

        except Exception as e:
            logger.error(f"❌ Execution failed: {e}")
            return None

    def stop(self):
        """Stop the scheduler"""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("✅ Scheduler stopped")

if __name__ == "__main__":
    scheduler = ForexScheduler()
    scheduler.start()

    # Keep running
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        scheduler.stop()
