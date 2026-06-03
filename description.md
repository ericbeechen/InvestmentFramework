# Investment Framework Codebase

## Purpose

This repository is an early-stage Python investment framework. It currently focuses on building a price universe for S&P 500 constituents, computing simple returns, and providing placeholders for client constraints, research views, risk, reporting, and trade workflow.

## Current Status

- The main runnable path builds a market universe and prints data to the console.
- Several modules are placeholders with empty class shells.
- A legacy prototype pipeline lives under Old/ and is not wired into the main entrypoint.

## Primary Workflow (Current)

1. main.py constructs a PortfolioConstructor and calls construct_portfolio.
2. PortfolioConstructor creates MarketData, ResearchViews, and ClientProfile instances.
3. MarketData.build_universe:
   - Reads a cached Excel file from yfinance_data if it exists.
   - Otherwise pulls S&P 500 constituents from a public CSV and downloads adjusted close prices via yfinance.
4. MarketData.universe_returns computes simple percent change returns and drops the first NaN row.
5. PortfolioConstructor prints the universe and return series. Future steps are left as commented placeholders.

## Data Sources and Inputs

- S&P 500 constituents: CSV from datahub.io.
- Prices: yfinance download for the selected period.
- Macro series: FRED GDP series via fredapi (requires FRED_API_KEY environment variable).

## Outputs and Artifacts

- Cached universe files at yfinance_data/universe_{period}.xlsx.
- Console output of the universe DataFrame and its return series.

## Runtime Requirements

- Python >= 3.13
- Key dependencies: pandas, yfinance, fredapi, openpyxl, lxml

## Module Map (Actual Behavior)

- ClientProfile.py: placeholder ClientProfile class, no fields or logic yet.
- MarketData.py: pulls S&P 500 constituents, downloads price history, caches Excel, computes returns, and exposes a FRED GDP helper.
- PortfolioConstructor.py: orchestrates MarketData and prints universe and returns; contains commented next steps.
- ResearchViews.py: placeholder ResearchViews class, no logic yet.
- PortfolioReporter.py: empty placeholder file.
- RiskEngine.py: empty placeholder file.
- TradeBlotter.py: empty placeholder file.

## Legacy Prototype (Old/)

The Old/ folder contains a prior pipeline that is not used by the main entrypoint:

- DataIngestion.py: Excel loader helper.
- PortfolioConstruction.py: equal weight or tangency weight calculator and simple performance stats.
- RiskControls.py: placeholder class shell.
- main copy.py: example script that loads Excel data and runs the legacy portfolio construction.

## Testing

No automated tests are included yet.
