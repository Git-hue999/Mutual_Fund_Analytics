
"""
Load processed mutual fund datasets into the SQLite database.
"""

import pandas as pd
from sqlalchemy import create_engine

# Creating SQLite Database:

engine = create_engine("sqlite:///bluestock_mf.db")

print("=" * 60)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 60)

# Listing of cleaned datasets:

datasets = {
    "fund_master": "Data/Raw/01_fund_master.csv",
    "nav_history": "Data/Processed/nav_history_cleaned.csv",
    "investor_transactions": "Data/Processed/investor_transactions_cleaned.csv",
    "scheme_performance": "Data/Processed/scheme_performance_cleaned.csv",
    "aum_by_fund_house": "Data/Raw/03_aum_by_fund_house.csv"
}

# Loading each CSV into SQLite:

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name:<25} Rows: {len(df)}")

print("\nAll datasets loaded successfully!")

print("\nVerifying row counts...")

for table_name in datasets.keys():

    rows = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM {table_name}",
        engine
    )

    print(f"{table_name:<25} {rows.iloc[0,0]} rows")

print("\nSQLite database created successfully!")