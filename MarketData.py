import os
import pandas as pd
import yfinance as yf
import fredapi as Fred

class MarketData:
    def __init__(self):
        self.securities: list[str] = []
        self.universe: pd.DataFrame | None = None
        self.returns: pd.DataFrame | None = None

    def pull_SP500_constituents(self):
        sp500_table = pd.read_csv("https://datahub.io/core/s-and-p-500-companies/r/constituents.csv")
        sp500_list = sp500_table["Symbol"].dropna().astype(str).str.replace(".", "-", regex=False).tolist()
        self.securities = sp500_list
        return self.securities

    def build_universe(self, period: str = "5y", file_path: str | None = None) -> pd.DataFrame:
        output_file = file_path or f"yfinance_data/universe_{period}.xlsx"

        if os.path.exists(output_file):
            self.universe = pd.read_excel(output_file, index_col=0, parse_dates=True)
            return self.universe
        
        self.pull_SP500_constituents()

        # period can be 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, ytd, max
        download = yf.download(self.securities, period = period, auto_adjust=False)
        
        if download is None:
            raise ValueError("No market data returned from yfinance.")

        adj_close = download["Adj Close"]

        # col_name = self.securities[0] if len(self.securities) == 1 else "Adj Close"
        sp500_df = adj_close

        sp500_df.to_excel(output_file)
        self.universe = sp500_df
        # print(f'Universe of assets: {universe}')
        return sp500_df
    
    def universe_returns(self, universe: pd.DataFrame) -> pd.DataFrame:
        returns = universe.pct_change(fill_method=None).iloc[1:]
        self.returns = returns
        # Add ability to annualize returns
        # print(f'Universe returns: {returns}')
        return returns


    def get_stock(self, ticker, start, end):
        stock_data = yf.download(ticker, start=start, end=end, auto_adjust=False)
        return stock_data

    def get_gdp(self, start, end):
        gdp_data = Fred.Fred(os.getenv('FRED_API_KEY')).get_series('GDP', start, end)
        return gdp_data

    
# MarketData = MarketData()
# print(MarketData.get_stock('AAPL', '2020-01-01', '2020-12-31'))


# dat = yf.Ticker("MSFT")
# # print(dat.info)
# print(dat.calendar)
# print(dat.analyst_price_targets)
# print(dat.quarterly_income_stmt)
# print(dat.history(period='1mo'))
# print(dat.option_chain(dat.options[0]).calls)

# tickers = yf.Tickers('MSFT AAPL GOOG')
# # print(tickers.tickers['MSFT'].info)
# print(yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo'))

# spy = yf.Ticker('SPY').funds_data
# print(spy.top_holdings)