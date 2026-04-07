import pandas as pd
import ResearchViews
from typing import Dict, List, Any

class Portfolio:
    def __init__(self, research: Any = ResearchViews.ResearchViews(), initial_cash: float = 1_000_000.0, cash_threshold: float = 0.01):
        self.initial_cash = initial_cash
        self.cash_threshold = cash_threshold * self.initial_cash
        self.research = research
        self.transaction_fee = 0.001

        self.cash: float = self.initial_cash
        self.holdings: Dict[str, int] = {}
        self.history: pd.DataFrame = pd.DataFrame()

    def _execute_buys(self, prices: pd.Series, views: pd.Series):
        buy_reccs = views[views > 1].sort_values(ascending=False)

        if buy_reccs.empty or self.cash <= self.cash_threshold:
            return
        
        available_to_invest = self.cash - self.cash_threshold
        ticker_budget = available_to_invest / len(buy_reccs)

        for ticker in buy_reccs.index:
            if self.cash <= self.cash_threshold:
                break

            price = prices.get(ticker)
            if pd.isna(price) or price <= 0:
                continue

            unit_cost = float(price) * (1 + self.transaction_fee)

            max_allot = int((self.cash - self.cash_threshold) // unit_cost)
            target_qty = int(ticker_budget // unit_cost)
            quantity = min(max_allot, target_qty)

            if quantity > 0:
                transaction_cost = self._transaction_costs(price, quantity)
                self.holdings[ticker] = self.holdings.get(ticker, 0) + quantity
                self.cash -= (quantity * float(price)) + transaction_cost

    def _execute_sells(self, prices: pd.Series, views: pd.Series):
        sell_reccs = views[views < -1].sort_values(ascending=False)

        if sell_reccs.empty:
            return

        for ticker in sell_reccs.index:
            price = prices.get(ticker)
            if pd.isna(price) or price <= 0:
                continue

            current_qty = self.holdings.get(ticker, 0)
            if current_qty <= 0:
                continue

            quantity = current_qty

            if quantity > 0:
                transaction_cost = self._transaction_costs(price, quantity)
                self.holdings[ticker] = self.holdings.get(ticker, 0) - quantity
                self.cash += (quantity * float(price)) - transaction_cost
    

    def _calc_value(self, prices: pd.Series) -> float:
        invested_value = 0.0
        for ticker, qty in self.holdings.items():
            if qty > 0:
                price = prices.get(ticker)
                if pd.notna(price) and price > 0:
                    invested_value += qty * float(price)
        return invested_value

    def _call_views(self, universe: pd.DataFrame) -> pd.DataFrame:
        return self.research.test_views().reindex(index=universe.index, columns=universe.columns)
    
    def _transaction_costs(self, price: float, quantity: int) -> float:
        return ((price * self.transaction_fee) * quantity)


    def backtest(self, universe: pd.DataFrame, frequency: str = 'D') -> pd.DataFrame:

        if frequency == 'D':
            universe = universe
        elif frequency == 'W':
            universe = universe.resample('W-MON').first()
        elif frequency == 'M':
            universe = universe.resample('BMS').first()
        else:
            universe = universe.resample('BQS').first()

        views = self._call_views(universe)
        portfolio_history: List[Dict[str, float]] = []

        self.cash = self.initial_cash
        self.holdings = {ticker: 0 for ticker in universe.columns}

        for date, prices_on_date in universe.iterrows():
            views_on_date = views.loc[date]

            self._execute_buys(prices_on_date, views_on_date)
            self._execute_sells(prices_on_date, views_on_date)

            invested_value = self._calc_value(prices_on_date)
            portfolio_value = self.cash + invested_value

            portfolio_history.append({
                "Date": date,
                "Cash": self.cash,
                "InvestedValue": invested_value,
                "PortfolioValue": portfolio_value,
            })


        self.history = pd.DataFrame(portfolio_history).set_index("Date")
        return self.history

