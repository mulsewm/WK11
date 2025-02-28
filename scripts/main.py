#!/usr/bin/env python3
"""
This script is a placeholder for data extraction, cleaning, and exploratory analysis for Task 1.
You will use this file to write your Python code that fetches data from YFinance, cleans it,
and performs exploratory analysis.
"""
import yfinance as yf
import pandas as pd

def fetch_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

if __name__ == "__main__":
    # Example usage: fetching TSLA data
    tsla_data = fetch_data("TSLA", "2015-01-01", "2025-01-31")
    print(tsla_data.head())
