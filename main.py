from Universe import Universe
from Portfolio import Portfolio
from Reporter import Reporter

def main():
    universe_builder = Universe()
    universe = universe_builder.construct_universe()
    # returns = universe_builder.construct_returns()

    portfolio = Portfolio()
    portfolio.backtest(universe, 'D')
    daily = portfolio.history
    portfolio.backtest(universe, 'W')
    weekly = portfolio.history
    portfolio.backtest(universe, 'M')
    monthly = portfolio.history
    portfolio.backtest(universe, 'Q')
    quarterly = portfolio.history
    reporter = Reporter()
    # reporter.plot(portfolio.history)
    reporter.plot_dfs([daily, weekly, monthly, quarterly], labels=['D', 'W', 'M', 'Q'])

if __name__ == "__main__": 
    main()
