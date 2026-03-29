import MarketData
import ResearchViews
import ClientProfile

class PortfolioConstructor:
    # This class will be responsible for constructing the portfolio based on market data, research views, and client profile.

    def __init__(self):
        self.market_data = MarketData.MarketData()
        self.research_views = ResearchViews.ResearchViews()
        self.client_profile = ClientProfile.ClientProfile()

    def construct_portfolio(self):
        print('Building universe of assets...')
        universe = self.market_data.build_universe()
        returns = self.market_data.universe_returns()
        print(f'Universe of assets: {universe}')
        print(f'Universe returns: {returns}')
        # Step 1: Build Universe of Assets
        # Step 2: Gather research views on the assets in the universe. e.g. which names or sectors to overweight or underweight, and which factors to tilt towards or away from.
        # Step 3: Filter assets based on client profile and research views
        # Step 4: Construct portfolio based on the above data


portfolio = PortfolioConstructor()
portfolio.construct_portfolio()