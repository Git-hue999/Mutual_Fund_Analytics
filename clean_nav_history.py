
"""
Clean and standardize mutual fund NAV history data.
"""

import pandas as pd

# Loading dataset:
df = pd.read_csv("Data/Raw/08_investor_transactions.csv")

print("=" * 60)
print("INVESTOR TRANSACTIONS CLEANING")
print("=" * 60)

print("Original Shape:", df.shape)

# Check missing values:
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows:
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

# Convert transaction_date to datetime (if present)
if "transaction_date" in df.columns:
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"], errors="coerce"
    )

# Remove records with invalid or non-positive transaction amounts
if "transaction_amount" in df.columns:
    df = df[df["transaction_amount"] > 0]

# Save cleaned dataset
output_path = "Data/Processed/investor_transactions_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nDuplicates Removed:", duplicates)
print("Final Shape:", df.shape)
print("Saved to:", output_path)