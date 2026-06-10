import os
import logging
from typing import Dict, Any, Optional
from datetime import datetime
from src.broker.client import OANDAClient
from src.db.models import Operation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

class TradeExecutor:
    """Executes trades based on signals from analysis engine"""

    def __init__(self, account_id: Optional[str] = None, access_token: Optional[str] = None,
                 environment: str = "practice", db_url: str = "sqlite:///quotes.db"):
        """
        Initialize executor

        Args:
            account_id: OANDA account ID
            access_token: OANDA API token
            environment: 'practice' or 'live'
            db_url: Database connection string
        """
        self.client = OANDAClient(account_id, access_token, environment)
        self.environment = environment
        self.db_url = db_url

        # Setup database session
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        self.db_session = Session()

        logger.info(f"TradeExecutor initialized - Environment: {environment}")

    def calculate_position_size(self, pair: str, entry_price: float, stop_loss: float,
                               risk_percentage: float = 0.8) -> float:
        """
        Calculate position size based on risk management

        Args:
            pair: Currency pair (e.g., "EUR_USD")
            entry_price: Entry price
            stop_loss: Stop loss price
            risk_percentage: % of equity to risk

        Returns:
            Position size in units
        """
        account_info = self.client.get_account_info()
        if not account_info:
            logger.error("Failed to get account info")
            return 0

        equity = float(account_info['account']['balance'])
        risk_amount = equity * (risk_percentage / 100)

        # Calculate distance to stop loss
        if pair.endswith('JPY') or pair.startswith('JPY'):
            # JPY pairs have different pip value
            pip_value = 0.01
        else:
            pip_value = 0.0001

        distance_to_sl = abs(entry_price - stop_loss)
        pips = distance_to_sl / pip_value

        # Position size = risk amount / (pips * pip value in target currency)
        if pips == 0:
            return 0

        # Simplified: assuming 1 lot = 100,000 units
        position_size = risk_amount / (distance_to_sl * 100000)

        # Round to nearest 0.01 lot
        position_size = round(position_size, 2)

        logger.info(f"{pair}: Risk=${risk_amount:.2f}, Distance={pips:.0f}pips, Size={position_size:.2f}lots")

        return position_size

    def execute_signal(self, signal: Dict[str, Any], pair: str) -> Dict[str, Any]:
        """
        Execute a trading signal

        Args:
            signal: Dictionary with keys:
                   - direction: 'LONG' or 'SHORT'
                   - entry_price: Entry price
                   - stop_loss: Stop loss price
                   - take_profit: Take profit price
                   - confidence: Confidence level (0-1)
            pair: Currency pair (e.g., "EUR_USD")

        Returns:
            Execution result
        """
        direction = signal['direction']
        entry_price = signal['entry_price']
        stop_loss = signal['stop_loss']
        take_profit = signal['take_profit']
        confidence = signal.get('confidence', 0.5)

        logger.info(f"\n{'='*60}")
        logger.info(f"Executing Signal - {pair} {direction}")
        logger.info(f"{'='*60}")
        logger.info(f"Entry: {entry_price:.5f}, SL: {stop_loss:.5f}, TP: {take_profit:.5f}")
        logger.info(f"Confidence: {confidence:.0%}")

        # Calculate position size
        position_size = self.calculate_position_size(pair, entry_price, stop_loss)

        if position_size == 0:
            logger.warning(f"Position size is 0, skipping execution")
            return {
                'status': 'failed',
                'reason': 'Invalid position size'
            }

        # Execute on OANDA
        if self.environment == "live":
            # WARNING: Real money execution
            logger.warning(f"⚠️  EXECUTING REAL TRADE - {pair} {direction} {position_size:.2f}lots")
        else:
            logger.info(f"[PRACTICE MODE] Would execute: {pair} {direction} {position_size:.2f}lots")

        # Place order
        oanda_direction = "BUY" if direction == "LONG" else "SELL"
        oanda_volume = int(position_size * 100000)  # Convert lots to units

        order_result = self.client.place_order(
            pair=pair,
            direction=oanda_direction,
            volume=oanda_volume,
            stop_loss=stop_loss,
            take_profit=take_profit
        )

        if not order_result:
            logger.error("Order placement failed")
            return {
                'status': 'failed',
                'reason': 'Order placement failed',
                'oanda_response': None
            }

        # Extract order info
        order_data = order_result.get('orderCreateTransaction', {})
        order_id = order_data.get('id')

        # Save to database
        try:
            operation = Operation(
                pair=pair,
                direction=direction,
                entry_price=entry_price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                entry_time=datetime.now(),
                status='OPEN',
                volume=oanda_volume / 100000  # Store in lots
            )
            self.db_session.add(operation)
            self.db_session.commit()

            logger.info(f"✅ Trade executed successfully")
            logger.info(f"Order ID: {order_id}, Size: {position_size:.2f}lots")

            return {
                'status': 'success',
                'pair': pair,
                'direction': direction,
                'volume': position_size,
                'entry_price': entry_price,
                'stop_loss': stop_loss,
                'take_profit': take_profit,
                'order_id': order_id,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Database error: {e}")
            return {
                'status': 'partial',
                'reason': f'Order placed but DB save failed: {e}',
                'order_id': order_id
            }

    def close_position(self, pair: str) -> Dict[str, Any]:
        """Close an open position"""
        try:
            operation = self.db_session.query(Operation).filter(
                Operation.pair == pair,
                Operation.status == 'OPEN'
            ).first()

            if not operation:
                logger.warning(f"No open position found for {pair}")
                return {'status': 'not_found'}

            # Close position via OANDA
            logger.info(f"Closing position: {pair}")

            operation.status = 'CLOSED'
            operation.exit_time = datetime.now()
            operation.exit_price = 0  # TODO: Get current price from market
            operation.pnl = 0  # TODO: Calculate PnL

            self.db_session.commit()

            return {
                'status': 'success',
                'pair': pair,
                'closed_at': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Error closing position: {e}")
            return {'status': 'error', 'reason': str(e)}

    def get_open_positions(self) -> list:
        """Get all open positions from database"""
        try:
            positions = self.db_session.query(Operation).filter(
                Operation.status == 'OPEN'
            ).all()

            return [
                {
                    'id': p.id,
                    'pair': p.pair,
                    'direction': p.direction,
                    'entry_price': p.entry_price,
                    'stop_loss': p.stop_loss,
                    'take_profit': p.take_profit,
                    'entry_time': p.entry_time.isoformat() if p.entry_time else None,
                    'volume': p.volume
                }
                for p in positions
            ]
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return []

    def get_operation_history(self, pair: str = None, limit: int = 100) -> list:
        """Get operation history"""
        try:
            query = self.db_session.query(Operation)

            if pair:
                query = query.filter(Operation.pair == pair)

            operations = query.order_by(Operation.entry_time.desc()).limit(limit).all()

            return [
                {
                    'id': op.id,
                    'pair': op.pair,
                    'direction': op.direction,
                    'entry_price': op.entry_price,
                    'exit_price': op.exit_price,
                    'entry_time': op.entry_time.isoformat() if op.entry_time else None,
                    'exit_time': op.exit_time.isoformat() if op.exit_time else None,
                    'status': op.status,
                    'pnl': op.pnl
                }
                for op in operations
            ]
        except Exception as e:
            logger.error(f"Error fetching history: {e}")
            return []

    def sync_with_broker(self) -> Dict[str, Any]:
        """Sync database with actual broker positions"""
        logger.info("Syncing with broker...")

        open_orders = self.client.get_open_orders()
        if not open_orders:
            return {'status': 'error', 'reason': 'Could not fetch open orders'}

        # TODO: Match DB positions with broker positions
        # For now, just log

        return {
            'status': 'success',
            'open_orders': len(open_orders.get('orders', []))
        }
