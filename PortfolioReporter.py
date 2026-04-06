import pandas as pd
import matplotlib.pyplot as plt


class PortfolioReporter:
    def __init__(self):
        pass


    def plot(self, portfolio):
        portfolio = portfolio.copy()
        plt.figure(figsize=(10, 6))
        cumulative_return = (1 + portfolio['Return']).cumprod() - 1
        plt.plot(cumulative_return, label='Cumulative Return')
        plt.title('Portfolio Return Over Time')
        plt.xlabel('Date')
        plt.ylabel('Return')
        plt.legend()
        plt.show() 