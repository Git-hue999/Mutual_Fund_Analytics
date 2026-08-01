# Mutual Fund Analytics - Data Dictionary

## 1. fund_master:

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct/Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio (%) |
| exit_load_pct | Float | Exit load (%) |
| min_sip_amount | Integer | Minimum SIP investment |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager |
| risk_category | Text | Risk classification |
| sebi_category_code | Text | SEBI category code |

---

## 2. nav_history:

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Scheme code |
| nav_date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 3. investor_transactions:

| Column | Type | Description |
|---------|------|-------------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme code |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | City classification |
| age_group | Text | Investor age group |
| gender | Text | Gender |
| annual_income_lakh | Float | Annual income |
| payment_mode | Text | Payment method |
| kyc_status | Text | KYC verification status |

---

## 4. scheme_performance:

| Column | Type | Description |
|---------|------|-------------|
| return_1yr_pct | Float | 1-year return |
| return_3yr_pct | Float | 3-year return |
| return_5yr_pct | Float | 5-year return |
| alpha | Float | Alpha value |
| beta | Float | Beta value |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annualized standard deviation |
| max_drawdown_pct | Float | Maximum drawdown |
| aum_crore | Float | Assets under management |
| expense_ratio_pct | Float | Expense ratio |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Text | Risk grade |

---

## 5. aum_by_fund_house:

| Column | Type | Description |
|---------|------|-------------|
| fund_house | Text | Mutual fund company |
| aum_crore | Float | Total assets under management |
