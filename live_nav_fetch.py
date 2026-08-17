
"""
Fetch and store the latest available mutual fund NAV data.
"""

import requests
import pandas as pd

schemes = {
    "125497": "hdfc_top_100",
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_large_cap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip",
}

for code, name in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])
    df["scheme_code"] = code
    df["scheme_name"] = data["meta"]["scheme_name"]

    filename = f"Data/raw/live_nav_{name}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {filename} — {len(df)} rows")