import PortfolioConstructor
import PortfolioReporter

def main():
    portfolio_constructor = PortfolioConstructor.PortfolioConstructor()
    portfolio = portfolio_constructor.construct_portfolio()
    portfolio_reporter = PortfolioReporter.PortfolioReporter()
    portfolio_reporter.plot(portfolio)


if __name__ == "__main__": 
    main()
