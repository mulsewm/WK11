#!/usr/bin/env python3
"""
data_preprocessing.py

This script fetches historical data for TSLA, BND, and SPY using YFinance,
performs data cleaning and basic exploratory analysis, and saves cleaned data
for further tasks.
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.makedirs("data", exist_ok=True)
# tsla_df.to_csv("data/TSLA_cleaned.csv", index=False)
# print("Saved TSLA cleaned data to data/TSLA_cleaned.csv")

# Set the plotting style
sns.set(style="whitegrid")

# Define function to fetch data for a given ticker
def fetch_data(ticker, start_date="2015-01-01", end_date="2025-01-31"):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)  # Convert Date index to a column
    return data

# List of tickers to download
tickers = ["TSLA", "BND", "SPY"]

# Dictionary to store dataframes
data_dict = {}

for ticker in tickers:
    df = fetch_data(ticker)
    data_dict[ticker] = df
    print(f"{ticker} data shape: {df.shape}")

# Inspect and clean the data: Check for missing values
for ticker, df in data_dict.items():
    print(f"\n{ticker} DataFrame Info:")
    print(df.info())
    missing = df.isnull().sum()
    print(f"Missing values in {ticker}:\n{missing}")

    # Example: Fill missing values using forward fill method (if needed)
    if missing.any():
        df.fillna(method='ffill', inplace=True)
        print(f"Missing values for {ticker} have been forward-filled.")

# Exploratory Data Analysis (using TSLA as an example)

# Plot TSLA Closing Price over time
tsla_df = data_dict["TSLA"]
plt.figure(figsize=(12, 6))
plt.plot(tsla_df['Date'], tsla_df['Close'], label="TSLA Close Price")
plt.title("TSLA Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.tight_layout()
plt.show()

# Calculate and plot the daily percentage change for TSLA
tsla_df['Daily_Pct_Change'] = tsla_df['Close'].pct_change()
plt.figure(figsize=(12, 6))
plt.plot(tsla_df['Date'], tsla_df['Daily_Pct_Change'], label="TSLA Daily % Change")
plt.title("TSLA Daily Percentage Change")
plt.xlabel("Date")
plt.ylabel("Daily % Change")
plt.legend()
plt.tight_layout()
plt.show()

# Calculate rolling statistics (30-day window) for TSLA
tsla_df['Rolling_Mean'] = tsla_df['Close'].rolling(window=30).mean()
tsla_df['Rolling_Std'] = tsla_df['Close'].rolling(window=30).std()

plt.figure(figsize=(12, 6))
plt.plot(tsla_df['Date'], tsla_df['Close'], label="Close Price")
plt.plot(tsla_df['Date'], tsla_df['Rolling_Mean'], label="30-Day Rolling Mean", linestyle='--')
plt.plot(tsla_df['Date'], tsla_df['Rolling_Std'], label="30-Day Rolling Std", linestyle=':')
plt.title("TSLA Rolling Statistics")
plt.xlabel("Date")
plt.ylabel("Price / Statistic")
plt.legend()
plt.tight_layout()
plt.show()

# Save the cleaned TSLA data to CSV for further analysis
tsla_df.to_csv("data/TSLA_cleaned.csv", index=False)
print("Saved TSLA cleaned data to data/TSLA_cleaned.csv")
