import os
import pandas as pd
import yfinance as yf
import fredapi as Fred
import datetime

class MarketData:
    def __init__(self):
        pass

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