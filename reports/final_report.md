# Time Series Forecasting for Portfolio Management Optimization

**Author:** Mulusew M. Tesfaye  
**Date:** 04 Mar 2025

---

## Table of Contents
1. [Introduction](#introduction)
2. [Data Overview](#data-overview)
3. [Task 1: Data Preprocessing & EDA](#task-1-data-preprocessing--eda)
4. [Task 2: Time Series Forecasting](#task-2-time-series-forecasting)
5. [Task 3: Forecast Future Market Trends](#task-3-forecast-future-market-trends)
6. [Task 4: Portfolio Optimization](#task-4-portfolio-optimization)
7. [Results and Discussion](#results-and-discussion)
8. [Conclusion and Future Work](#conclusion-and-future-work)
9. [References](#references)

---

<a name="introduction"></a>
## 1. Introduction
Guide Me in Finance (GMF) Investments aims to leverage advanced time series forecasting techniques to optimize portfolio management. By analyzing historical data for three assets—Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and the S&P 500 ETF (SPY)—this project demonstrates how data-driven insights can inform better investment decisions.

**Business Objectives:**
- Predict market trends using time series models.
- Use forecasted insights to optimize asset allocation.
- Enhance portfolio returns while managing risk.

---

<a name="data-overview"></a>
## 2. Data Overview
- **Data Source:** YFinance (Jan 1, 2015 – Jan 31, 2025)
- **Assets:**
  - **TSLA:** High-volatility, growth-oriented stock.
  - **BND:** Low-risk bond ETF.
  - **SPY:** Diversified exposure to the U.S. equity market (S&P 500).
- **Features:** Date, Open, High, Low, Close, Adj Close, Volume, etc.

---

<a name="task-1-data-preprocessing--eda"></a>
## 3. Task 1: Data Preprocessing & EDA
### 3.1 Data Cleaning
- Handled missing values using forward-fill.
- Converted date columns to `datetime` format.
- Removed duplicates and ensured consistent data types.

### 3.2 Exploratory Data Analysis
- **Trend Analysis:**  
  - Visualized closing prices over time for each asset.
- **Volatility Analysis:**  
  - Computed daily percentage changes and rolling standard deviations.
- **Seasonal Decomposition:**  
  - Used statistical libraries (e.g., `statsmodels`) to identify trend, seasonal, and residual components.

**Key Insights:**
- TSLA shows higher volatility than BND and SPY.
- Clear upward trend for TSLA and SPY, while BND is relatively stable.

---

<a name="task-2-time-series-forecasting"></a>
## 4. Task 2: Time Series Forecasting
### 4.1 Model Selection
- Chose **ARIMA** (AutoRegressive Integrated Moving Average) for univariate time series forecasting.
- Compared different (p, d, q) parameters using `auto_arima` or grid search.

### 4.2 Model Training
- **Train/Test Split:** Data before 2024-12-31 for training, after for testing.
- **Parameter Optimization:**  
  - Tuned ARIMA parameters to minimize AIC/BIC or maximize forecast accuracy.
- **Evaluation Metrics:**  
  - **MAE, RMSE, MAPE** to measure prediction error.

### 4.3 Model Performance
- Show actual vs. predicted prices for TSLA, BND, and SPY.
- Summarize error metrics in a table.

---

<a name="task-3-forecast-future-market-trends"></a>
## 5. Task 3: Forecast Future Market Trends
### 5.1 Forecast Generation
- Generated 6–12 month forecasts using the final ARIMA models for each asset.
- Stored forecast results (date, predicted price) in CSV or DataFrame.

### 5.2 Forecast Visualization
- Plotted forecast curves alongside historical data.
- Included confidence intervals to reflect uncertainty.

**Observations:**
- TSLA’s forecast suggests continued volatility with a moderate upward trend.
- BND remains relatively stable, indicating low risk.
- SPY’s forecast aligns with overall market growth, but with seasonal dips.

---

<a name="task-4-portfolio-optimization"></a>
## 6. Task 4: Portfolio Optimization
### 6.1 Data Preparation
- Computed daily returns for TSLA, BND, and SPY.
- Created a combined dataframe of returns for optimization.

### 6.2 Modern Portfolio Theory (MPT)
- Calculated mean returns and covariance matrix.
- Ran an optimization algorithm (e.g., PyPortfolioOpt) to:
  - Maximize the **Sharpe Ratio**.
  - Identify optimal asset weights.

### 6.3 Results
- **Optimal Weights:** TSLA (x%), BND (y%), SPY (z%)
- **Expected Annual Return:** ~ X%
- **Volatility (Std Dev):** ~ Y%
- **Sharpe Ratio:** ~ Z

**Interpretation:**
- TSLA’s high volatility reduces its ideal weighting unless the forecast suggests strong growth.
- BND’s stability helps lower portfolio risk.
- SPY provides a diversified core holding.

---

<a name="results-and-discussion"></a>
## 7. Results and Discussion
- **Forecast Accuracy:** 
  - MAE, RMSE, MAPE demonstrate how well the model captures price movements.
- **Portfolio Performance:**
  - The optimized portfolio balances risk and return effectively.
  - Depending on market conditions, rebalancing might be necessary.

**Limitations:**
- Forecast models assume historical patterns will persist.
- External shocks (e.g., macroeconomic events) can drastically affect prices.

---

<a name="conclusion-and-future-work"></a>
## 8. Conclusion and Future Work
- **Achievements:** 
  - Demonstrated how time series forecasting can inform asset allocation.
  - Showed that including stable assets like BND can reduce overall portfolio volatility.

- **Next Steps:** 
  - Implement advanced models (e.g., LSTM) for potentially better accuracy.
  - Incorporate more assets for a broader diversification.
  - Use real-time data feeds for continuous portfolio rebalancing.

---

<a name="references"></a>
## 9. References
1. [ARIMA Modeling Guide](https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/)
2. [Portfolio Optimization](https://github.com/robertmartin8/PyPortfolioOpt)
3. [YFinance Documentation](https://pypi.org/project/yfinance/)

---

