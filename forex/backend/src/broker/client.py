import os
from datetime import datetime, timedelta
import pandas as pd
import requests

class OANDAClient:
    """OANDA v20 API Client"""

    def __init__(self, account_id=None, access_token=None, environment="practice"):
        self.account_id = account_id or os.getenv("OANDA_ACCOUNT_ID")
        self.access_token = access_token or os.getenv("OANDA_ACCESS_TOKEN")
        self.environment = environment

        if environment == "practice":
            self.base_url = "https://api-fxpractice.oanda.com"
        else:
            self.base_url = "https://api-fxtrade.oanda.com"

        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def get_quotes(self, pair, granularity="D", count=500):
        """
        Fetch historical candles
        granularity: M1, M5, H1, D, W, M
        """
        url = f"{self.base_url}/v3/instruments/{pair}/candles"
        params = {
            "granularity": granularity,
            "count": count
        }

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            data = response.json()
            candles = data.get("candles", [])

            ohlc_data = []
            for candle in candles:
                ohlc_data.append({
                    'timestamp': candle['time'],
                    'open': float(candle['mid']['o']),
                    'high': float(candle['mid']['h']),
                    'low': float(candle['mid']['l']),
                    'close': float(candle['mid']['c']),
                    'volume': int(candle.get('volume', 0))
                })

            df = pd.DataFrame(ohlc_data)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            return df

        except requests.exceptions.RequestException as e:
            print(f"Error fetching quotes: {e}")
            return None

    def get_account_info(self):
        """Get account balance and details"""
        url = f"{self.base_url}/v3/accounts/{self.account_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching account info: {e}")
            return None

    def place_order(self, pair, direction, volume, stop_loss, take_profit):
        """
        Place a market order
        direction: BUY or SELL
        """
        url = f"{self.base_url}/v3/accounts/{self.account_id}/orders"

        order_data = {
            "order": {
                "instrument": pair,
                "units": volume if direction == "BUY" else -volume,
                "type": "MARKET",
                "takeProfitOnFill": {
                    "price": str(take_profit)
                },
                "stopLossOnFill": {
                    "price": str(stop_loss)
                }
            }
        }

        try:
            response = requests.post(url, headers=self.headers, json=order_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error placing order: {e}")
            return None

    def get_open_orders(self):
        """Get all open orders"""
        url = f"{self.base_url}/v3/accounts/{self.account_id}/orders"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching open orders: {e}")
            return None

    @staticmethod
    def get_major_pairs():
        """Return list of major forex pairs"""
        return [
            "EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD",
            "USD_CAD", "NZD_USD", "EUR_GBP", "EUR_JPY", "EUR_CHF",
            "GBP_JPY", "AUD_JPY", "CAD_JPY", "NZD_JPY", "CHF_JPY",
            "AUD_NZD", "EUR_AUD", "EUR_NZD", "GBP_AUD", "GBP_NZD"
        ]
