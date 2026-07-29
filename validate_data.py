import pandas as pd

fund = pd.read_csv("Data/Raw/01_fund_master.csv")
nav = pd.read_csv("Data/Raw/02_nav_history.csv")

print("Validation Summary")
print(nav["amfi_code"].isin(fund["amfi_code"]).value_counts())

missing_codes = set(fund["amfi_code"]) - set(nav["amfi_code"])

print("\nMissing AMFI Codes:")
print(missing_codes)

print("Total Missing:", len(missing_codes))
