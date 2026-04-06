import MarketData
import ResearchViews
import ClientProfile
import pandas as pd

class PortfolioConstructor:
    # This class will be responsible for constructing the portfolio based on market data, research views, and client profile.

    def __init__(self):
        self.market_data = MarketData.MarketData()
        self.research_views = ResearchViews.ResearchViews()
        self.client_profile = ClientProfile.ClientProfile()

    def construct_portfolio(self):
        # Step 1: Build Universe of Assets
        print('Building universe of assets...')
        universe = self.market_data.build_universe()
        returns = self.market_data.universe_returns(universe) 
        # Step 2: Gather research views on the assets in the universe. e.g. which names or sectors to overweight or underweight, and which factors to tilt towards or away from.
        recommendations = self.research_views.test_views()
        # Step 3: Construct portfolio based on the above data
        positive_recommendations = recommendations.reindex_like(returns).gt(0)
        portfolio = returns.where(positive_recommendations, 0.0)
        active_positions = positive_recommendations.sum(axis=1)
        selected_returns_sum = portfolio.sum(axis=1)
        total_return = selected_returns_sum.div(active_positions.where(active_positions > 0), fill_value=0.0).fillna(0.0)
        portfolio["Return"] = total_return
        return portfolio


        
# portfolio = PortfolioConstructor()
# test = portfolio.construct_portfolio()
# print(test)
