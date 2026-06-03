import numpy as np
import pandas as pd

class ResearchViews:
    def __init__(self, output_file: str = f"yfinance_data/universe_5y.xlsx"):
        self.views: pd.DataFrame = pd.DataFrame()
        self.download = pd.read_excel(output_file, index_col=0, parse_dates=True).iloc[1:]

    def test_views(self):
        dates = self.download.index
        names = self.download.columns

        test_names = pd.DataFrame(np.random.normal(size=self.download.shape), index=dates,columns=names)

        self.views = test_names
        # print(self.views)
        return test_names
    
    def new_views(self, universe: pd.DataFrame) -> pd.DataFrame:
        dates = universe.index
        names = universe.columns

        return universe
