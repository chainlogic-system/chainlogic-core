import time
import random


class PaperExecutor:

    def __init__(self):
        self.balance = 10000
        self.positions = []
        self.trades = []

    def execute(self, symbol, action, lot):

        price = round(random.uniform(1.0, 1.5), 5)

        pnl = 0
        if action == "BUY":
            pnl = lot * random.uniform(-5, 10)
        elif action == "SELL":
            pnl = lot * random.uniform(-10, 5)

        trade = {
            "symbol": symbol,
            "action": action,
            "lot": lot,
            "price": price,
            "pnl": pnl,
            "timestamp": time.time()
        }

        self.trades.append(trade)
        self.balance += pnl

        return {
            "status": "EXECUTED_PAPER",
            "trade": trade,
            "balance": self.balance
        }

    def get_state(self):

        return {
            "balance": self.balance,
            "open_positions": len(self.positions),
            "total_trades": len(self.trades)
        }
