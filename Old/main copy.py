import DataIngestion
import PortfolioConstruction
import RiskControls

def main():
    # excess_returns = DataIngestion.DataIngestion("data/multi_asset_etf_data.xlsx", sheet_name="excess returns")
    # excess_returns_df = excess_returns.load_data()

    # total_returns = DataIngestion.DataIngestion("data/multi_asset_etf_data.xlsx", sheet_name="total returns")
    # total_returns_df = total_returns.load_data()

    total_returns = DataIngestion.DataIngestion("data/sector_etf_data.xlsx", sheet_name="total returns")
    total_returns_df = total_returns.load_data()

    portfolio = PortfolioConstruction.PortfolioConstruction(returns=total_returns_df)
    portfolio.construct_portfolio()
    stats = portfolio.summary_stats()
    print(stats)




if __name__ == "__main__":
    main()
