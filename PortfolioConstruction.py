import pandas as pd
import numpy as np

class PortfolioConstruction:
    def __init__(self, returns=None):
        self.returns = returns
        self.returns = self

    def calc_weights(self, method="equal"):
        if method == "equal":
            # basic equal weight
            weights = [1 / len(self.returns.columns)] * len(self.returns.columns)
        elif method == "tangency":
            weights = np.linalg.inv(self.returns.cov()).dot(self.returns.mean())
            weights /= weights.sum()
        return weights

    def construct_portfolio(self):
        self.weights = self.calc_weights("tangency")
        self.portfolio_returns = (self.returns * self.weights).sum(axis=1)
        return self
    
    def summary_stats(self, periods_per_year=12):
        mean = self.portfolio_returns.mean()
        vol = self.portfolio_returns.std()
        sharpe_annualized = (mean / vol) * np.sqrt(periods_per_year)
        cumulative_return = (1 + self.portfolio_returns).prod() - 1

        stats_df = pd.DataFrame({
            "annualized_return": mean * periods_per_year,
            "annualized_volatility": vol * np.sqrt(periods_per_year),
            "annualized_sharpe_ratio": sharpe_annualized,
            "cumulative_return": cumulative_return,
        }, index=['Portfolio'])
        return stats_df