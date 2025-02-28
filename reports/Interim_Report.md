# Interim Report – Task 1: Data Preprocessing, Cleaning, and Exploratory Analysis

## 1. Introduction
This report documents the initial phase of our project for Guide Me in Finance (GMF) Investments. In this phase, we focus on extracting historical financial data for three assets (TSLA, BND, SPY) using the YFinance library, cleaning and preprocessing the data, and conducting an exploratory data analysis (EDA) to uncover insights on trends, volatility, and seasonality.

## 2. Data Extraction
- **Data Source:** YFinance API  
- **Assets:**
  - **TSLA:** High-growth, high-volatility stock (Tesla).
  - **BND:** Stable bond ETF (Vanguard Total Bond Market ETF).
  - **SPY:** Broad U.S. market exposure via the S&P 500 ETF.
- **Period:** January 1, 2015 – January 31, 2025.
- **Method:** Data is fetched using a Python script (`data_preprocessing.py`), which downloads and resets the index for proper handling of date information.

## 3. Data Cleaning and Preprocessing
- **Data Inspection:**  
  - Verified that all columns have appropriate data types (dates as datetime objects, numerical values for prices and volumes).
  - Identified missing values using descriptive statistics.
- **Handling Missing Values:**  
  - Applied forward-fill to address any missing values.
- **Outlier Detection:**  
  - Utilized statistical methods (e.g., Z-score or IQR) to detect outliers, ensuring that any anomalies in daily returns are handled appropriately.
- **Normalization:**  
  - Considered normalization or scaling techniques, especially important when preparing data for machine learning models.

## 4. Exploratory Data Analysis (EDA)
- **Trend Analysis:**  
  - Visualized daily closing prices for TSLA, BND, and SPY over time.
  - Identified long-term trends and periodic patterns that are critical for forecasting.
- **Volatility Analysis:**  
  - Computed daily percentage changes, particularly for TSLA.
  - Calculated 30-day rolling mean and standard deviation to gauge short-term volatility.
- **Visualization:**  
  - Generated plots for TSLA’s closing prices, daily percentage changes, and rolling statistics.
  - These visualizations provide a clear picture of market behavior and highlight periods of high volatility.

## 5. Key Insights
- **Data Quality:**  
  - The dataset required standard cleaning with minimal missing data, which was effectively managed.
- **Asset Behavior:**  
  - TSLA shows significant volatility and upward trends, which implies a higher risk-reward profile.
  - BND and SPY appear more stable, providing a counterbalance in a diversified portfolio.
- **Implications for Future Tasks:**  
  - Insights from the EDA will be critical in shaping our forecasting models and subsequent portfolio optimization.

## 6. Next Steps
- **Extend EDA:**  
  - Apply similar analyses to BND and SPY.
  - Perform seasonal decomposition for all assets to further understand underlying patterns.
- **Model Development:**  
  - Develop time series forecasting models (using ARIMA, SARIMA, or LSTM) based on the cleaned data.
- **Portfolio Optimization:**  
  - Utilize forecasted data in the next phase to optimize asset allocation.
- **Documentation:**  
  - Continue updating this report with insights, visualizations, and any challenges encountered during further analysis.

## 7. Repository Structure and Scripts
- **Folder Structure:**  
  - `reports/` – Contains this interim report.
  - `scripts/` – Contains Python scripts, including `data_preprocessing.py`.
  - `data/` – Location for cleaned data files.
- **GitHub Repository:**  
  - All code and analysis outputs are version-controlled in our GitHub repository.  
  - [Your GitHub Repository Link](https://github.com/mulsewm/wk-11) 

---

This report marks the completion of Task 1 and sets the foundation for subsequent stages, including forecasting and portfolio optimization. The cleaned data and insights derived from this analysis will guide our next steps in developing predictive models and refining our investment strategies.
