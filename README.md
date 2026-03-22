# Clean and Compute Returns

Quant interview-style project: clean financial data and compute returns using Python libraries.

---

## Overview

You are given a messy financial time series dataset containing asset prices.

Your task is to clean the data and compute daily returns in a robust and reusable way.

This project simulates a real quant take-home assignment.

---

## Dataset

The dataset contains:
- `date`
- `ticker`
- `price`

The data may include:
- Missing values
- Duplicate rows
- Unsorted dates
- Inconsistent formatting

---

## Tasks

1. Load the dataset
2. Clean the data:
   - Handle missing values
   - Remove or resolve duplicates
   - Ensure correct sorting by date per ticker
3. Compute daily returns per ticker
4. Output a clean dataset with:
   - date
   - ticker
   - price
   - returns

---

## Requirements

- Use Python (pandas expected)
- Write clean, modular code
- Prefer vectorised operations where possible

---

## Deliverables

- A script or notebook that performs the full pipeline
- Cleaned dataset with computed returns
- Clear and reusable functions

---

## Evaluation Criteria

Your solution will be assessed on:

- Correctness of return calculations
- Handling of missing and inconsistent data
- Code clarity and structure
- Logical handling of edge cases

---

## Submission

1. Fork this repository
2. Complete the implementation
3. Push your solution to your GitHub

---

## Project Structure

data/
    raw/
        prices.csv
    processed/
        cleaned_prices_with_returns.csv

src/
    clean_returns.py

requirements.txt
README.md

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the pipeline:
   python src/clean_returns.py

3. Output will be saved to:
   data/processed/cleaned_prices_with_returns.csv
