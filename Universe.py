import MarketData
import pandas as pd

class Universe:
    # This class will be responsible for constructing the universe of assets based on market data.

    def __init__(self):
        self.market_data = MarketData.MarketData()
        self.universe = pd.DataFrame()
        self.returns = pd.DataFrame()

    def construct_universe(self):
        # Step 1: Build Universe of Assets
        print('Building universe of assets...')
        universe = self.market_data.build_universe()
        self.universe = universe
        return universe
    
    def construct_returns(self):
        print('Generating returns for universe of assets...')
        returns = self.market_data.universe_returns(self.universe) 
        self.returns = returns
        return returns


