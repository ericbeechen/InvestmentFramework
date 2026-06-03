import pandas as pd
import matplotlib.pyplot as plt


class Reporter:
    def __init__(self):
        pass

    def plot_df(self, portfolio: pd.DataFrame):
        portfolio = portfolio.copy()
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio['PortfolioValue'], label = 'Value')
        plt.title('Portfolio Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

    def plot_dfs(self, portfolios: list[pd.DataFrame], labels: list[str] | None = None): 
        plt.figure(figsize=(10, 6))
        if labels is None:
            labels = [f"Portfolio {i + 1}" for i in range(len(portfolios))]

        for portfolio, label in zip(portfolios, labels):
            plt.plot(portfolio['PortfolioValue'], label=label)
        plt.title('Portfolios Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()