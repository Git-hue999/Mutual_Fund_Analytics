import pandas as pd

# Load dataset
df = pd.read_csv("Data/Raw/07_scheme_performance.csv")

print("=" * 60)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 60)
print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove dupicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

# Convert return columns to numeric
return_columns = ["return_1y", "return_3y", "return_5y"]

for col in return_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Expense ratio validation:
if "expense_ratio_pct" in df.columns:
    invalid_expense = df[
        (df["expense_ratio_pct"] < 0.1) |
        (df["expense_ratio_pct"] > 2.5)
    ]

    print("\nInvalid Expense Ratio Records:")
    print(len(invalid_expense))

# Save cleaned dataset
output_path = "Data/Processed/scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nDuplicates Removed:", duplicates)
print("Final Shape:", df.shape)
print("Saved to:", output_path)
