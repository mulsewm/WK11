#!/bin/bash
# init_repo.sh
# This script sets up the folder structure and initial files for the interim report deliverables,
# then makes the first Git commit and pushes it to the remote repository.

# Define folder structure
FOLDERS=(
  "reports"
  "data"
  "scripts"
  "notebooks"
)

# Create folders
for folder in "${FOLDERS[@]}"; do
  mkdir -p "$folder"
  echo "Created folder: $folder"
done

# Create initial files with basic content

# README.md with project overview
cat <<EOF > README.md
# GMF Investments Challenge - Interim Report Deliverables

This repository contains the deliverables for the Guide Me in Finance (GMF) Investments challenge.
The current focus is on Task 1: Data Preprocessing, Cleaning, and Exploratory Analysis.
EOF
echo "Created README.md"

# Interim report markdown file
cat <<EOF > reports/Interim_Report.md
# Interim Report – Task 1
**Data Preprocessing, Cleaning, and Exploratory Analysis**

**Deadline:** 20:00 UTC on Friday, 28 Feb 2025  
**GitHub Code:** [Repository Link](#)

---

## 1. Introduction
*Provide an overview of the project and the objectives of Task 1.*

## 2. Data Extraction
*Describe the data source (YFinance), date range, and key assets (TSLA, BND, SPY).*

## 3. Data Cleaning and Preprocessing
*Outline the steps taken for data type checks, missing value handling, and normalization.*

## 4. Exploratory Data Analysis (EDA)
*Detail your approach to trend analysis, volatility calculations, and seasonal decomposition.*

## 5. Key Insights & Summary
*Summarize the main insights from your exploratory analysis.*

EOF
echo "Created Interim_Report.md in reports"

# Placeholder Python script for data extraction and processing
cat <<EOF > scripts/main.py
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
EOF
chmod +x scripts/main.py
echo "Created main.py in scripts and set executable permissions"

# Create a basic .gitignore file
cat <<EOF > .gitignore
# Ignore Python cache files
__pycache__/
*.pyc

# Ignore data files (if needed)
data/

# Ignore notebook checkpoints
.ipynb_checkpoints/
EOF
echo "Created .gitignore"

# Create a requirements file listing key libraries
cat <<EOF > requirements.txt
yfinance
pandas
numpy
matplotlib
statsmodels
scikit-learn
EOF
echo "Created requirements.txt"

# Initialize Git repository if not already present
if [ ! -d ".git" ]; then
  git init
  echo "Initialized a new Git repository."
fi

# Stage all files and commit
git add .
git commit -m "Initial commit: Set up folder structure and files for interim report deliverables"

# Push to remote repository (ensure remote 'origin' is set up)
git push -u origin master

echo "Initial commit pushed to remote repository."
