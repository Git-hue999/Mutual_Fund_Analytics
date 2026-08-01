
-- Day 2 - Task 6
-- Mutual Fund Analytics SQL Queries


-- 1) Top 5 Funds by AUM:

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2) Average NAV:

SELECT
    AVG(nav) AS average_nav
FROM nav_history;


-- 3) Total Transactions by State:

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4) Funds with Expense Ratio below 1%:

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


-- 5) Average 1-Year Return:

SELECT
    AVG(return_1yr_pct) AS avg_return
FROM scheme_performance;


-- 6) Highest Sharpe Ratio:

SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 7) Investors by Gender:

SELECT
    gender,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY gender;


-- 8) Transaction Amount by Payment Mode:

SELECT
    payment_mode,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY payment_mode
ORDER BY total_amount DESC;


-- 9) Average Annual Income:

SELECT
    AVG(annual_income_lakh) AS avg_income
FROM investor_transactions;


-- 10) Top Risk Categories:

SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM fund_master
GROUP BY risk_category
ORDER BY total_funds DESC;

--***--