import os
from datetime import date
import ClientProfile
import MarketData
import PortfolioConstructor
import ResearchViews
import RiskEngine
import PortfolioReporter
import TradeBlotter


def _print_section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def demo() -> None:
    print(f"Investment Framework demo - {date.today().isoformat()}")

    _print_section("Core workflow: portfolio construction")
    portfolio = getattr(PortfolioConstructor, "portfolio", None)
    if portfolio is None:
        portfolio = PortfolioConstructor.PortfolioConstructor()
        portfolio.construct_portfolio()
    else:
        print("PortfolioConstructor already ran on import; reusing existing instance.")

    _print_section("Market data examples")
    market_data = getattr(portfolio, "market_data", None) or MarketData.MarketData()
    universe = market_data.universe if market_data.universe is not None else market_data.build_universe(period="1y")
    returns = market_data.returns if market_data.returns is not None else market_data.universe_returns()
    print(f"Universe shape: {universe.shape}")
    print(f"Return series shape: {returns.shape}")

    sample_ticker = "AAPL"
    stock_data = market_data.get_stock(sample_ticker, start="2020-01-01", end="2020-12-31")
    print(f"{sample_ticker} rows: {len(stock_data)}")

    if os.getenv("FRED_API_KEY"):
        gdp = market_data.get_gdp("2015-01-01", "2020-12-31")
        print(f"GDP series rows: {len(gdp)}")
    else:
        print("Skipping GDP: set FRED_API_KEY to enable macro data.")

    _print_section("Placeholders: client, research, risk, reporting, trade")
    client = ClientProfile.ClientProfile()
    research = ResearchViews.ResearchViews()
    print(f"ClientProfile initialized: {client.__class__.__name__}")
    print(f"ResearchViews initialized: {research.__class__.__name__}")

    if hasattr(RiskEngine, "RiskEngine"):
        print("RiskEngine initialized: RiskEngine")
    else:
        print("RiskEngine module present; class not implemented yet.")

    if hasattr(PortfolioReporter, "PortfolioReporter"):
        print("PortfolioReporter initialized: PortfolioReporter")
    else:
        print("PortfolioReporter module present; class not implemented yet.")

    if hasattr(TradeBlotter, "TradeBlotter"):
        print("TradeBlotter initialized: TradeBlotter")
    else:
        print("TradeBlotter module present; class not implemented yet.")
    print("\nDemo complete.")

def main():
    _print_section("Core workflow: portfolio construction")
    portfolio = getattr(PortfolioConstructor, "portfolio", None)
    if portfolio is None:
        portfolio = PortfolioConstructor.PortfolioConstructor()
        portfolio.construct_portfolio()
    else:
        print("PortfolioConstructor already ran on import; reusing existing instance.")

    _print_section("Market data examples")
    market_data = getattr(portfolio, "market_data", None) or MarketData.MarketData()
    universe = market_data.universe if market_data.universe is not None else market_data.build_universe(period="1y")
    returns = market_data.returns if market_data.returns is not None else market_data.universe_returns()
    print(f"Universe shape: {universe.shape}")
    print(f"Return series shape: {returns.shape}")

    sample_ticker = "AAPL"
    stock_data = market_data.get_stock(sample_ticker, start="2020-01-01", end="2020-12-31")

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
    # demo()
    main()
