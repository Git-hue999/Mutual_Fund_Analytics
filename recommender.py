import pandas as pd

funds = pd.read_csv(
    "Data/Processed/scheme_performance_cleaned.csv"
)

def recommend_funds(risk_grade, top_n=3):

    result = funds[
        funds["risk_grade"].astype(str).str.strip().str.lower()
        == risk_grade.strip().lower()
    ].copy()

    return result.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(top_n)[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]
