import os
import numpy as np
import pandas as pd

class ResearchViews:
    def __init__(self):
        self.views: pd.DataFrame = pd.DataFrame()

    def test_views(self):
        output_file = f"yfinance_data/universe_1y.xlsx"
        download = pd.read_excel(output_file, index_col=0, parse_dates=True).iloc[1:]

        dates = download.index
        names = download.columns

        test_names = pd.DataFrame(np.random.normal(size=download.shape), index=dates,columns=names)

        self.views = test_names
        # print(self.views)
        return test_names


# view = ResearchViews()
# testviews = view.test_views()
# print(testviews)