import MarketData
import ResearchViews
import ClientProfile

class PortfolioConstructor:
    def __init__(self):
        self.market_data = MarketData.MarketData()
        self.research_views = ResearchViews.ResearchViews()
        self.client_profile = ClientProfile.ClientProfile()

    def construct_portfolio(self):
        print('Constructing portfolio...')