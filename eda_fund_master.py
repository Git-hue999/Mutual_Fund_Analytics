import pandas as pd

# Load dataset
df = pd.read_csv("Data/Raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER DATASET SUMMARY")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFund Houses:")
print(df["fund_house"].value_counts())

print("\nCategories:")
print(df["category"].value_counts())

print("\nSub Categories:")
print(df["sub_category"].value_counts())

print("\nRisk Categories:")
print(df["risk_category"].value_counts())
