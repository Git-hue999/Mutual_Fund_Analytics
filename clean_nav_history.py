import pandas as pd

# Load dataset
df = pd.read_csv("Data/Raw/02_nav_history.csv")

print("=" * 60)
print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove duplicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

# Sort values
df = df.sort_values(["amfi_code", "date"])

# Forward fill NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Save cleaned dataset
output_path = "Data/Processed/nav_history_cleaned.csv"
df.to_csv(output_path, index=False)

print("Duplicates Removed:", duplicates)
print("Final Shape:", df.shape)
print("Saved to:", output_path)