USE customer_churn_retention;

-- ==========================================
-- 1. CHURN BY CONTRACT TYPE
-- ==========================================
SELECT 
    contract_type,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(total_revenue), 2) AS total_revenue
FROM customer_churn_retention.customers
GROUP BY contract_type
ORDER BY churn_rate_pct DESC;

/* 
BUSINESS INSIGHTS / CHURN ANALYSIS (CONTRACT TYPE):

1. UNIFORM CHURN RISK: 
   - Churn rate is virtually identical across all contract types: Yearly (10.34%), Monthly (10.33%), and Quarterly (9.93%).
   
2. REVENUE AT RISK:
   - Monthly contract holders represent the highest volume (4,967 customers) and the largest revenue pool ($5,239,430.00). 
   - With 513 churned monthly customers, this segment accounts for over half of all lost customers in this category.

3. STRATEGIC IMPLICATION:
   - Annual contracts are not providing the expected retention safety net compared to monthly plans.
   - Recommendation: Re-evaluate long-term contract incentives and introduce proactive renewal offers 60 days before contract expiration.
*/

-- ==========================================
-- 2. CHURN BY WEEKLY ACTIVE DAYS
-- ==========================================
SELECT 
    weekly_active_days,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn_retention.customers
GROUP BY weekly_active_days
ORDER BY weekly_active_days ASC;

/* 
BUSINESS INSIGHTS / CHURN ANALYSIS (WEEKLY ACTIVE DAYS):

1. ENGAGEMENT BENCHMARK:
   - Churn rate remains largely stable between 8.37% and 11.00% regardless of activity level.
   - Customers active 3 days per week show the lowest churn rate at 8.37% (101 churned customers).

2. HIGH-ACTIVITY CHURN PARADOX:
   - Highly active users (6-7 days/week) still churn at 9.17% to 10.82%, indicating that frequent usage alone does not guarantee long-term retention.
   - Low activity users (0-2 days/week) account for 413 total churned customers (approx. 40% of all churned users).

3. STRATEGIC IMPLICATION:
   - Automated re-engagement triggers should target users whose weekly activity drops below 3 days.
   - Recommendation: Investigate product friction points or service issues experienced by daily active users (6-7 days) who cancel despite high usage.
*/


-- ==========================================
-- 3. CHURN BY AGE BRACKET
-- ==========================================
SELECT 
    CASE 
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 50 THEN '30-50'
        ELSE '51+'
    END AS age_group,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn_retention.customers
GROUP BY age_group
ORDER BY churn_rate_pct DESC;
/* 
BUSINESS INSIGHTS / CHURN ANALYSIS (AGE GROUP):

1. HIGHEST DEMOGRAPHIC RISK (51+ GROUP):
   - The 51+ age demographic exhibits the highest churn rate at 10.39% (432 churned out of 4,157 total customers).
   - This group also represents the largest overall customer base, making them the single biggest contributor to absolute lost revenue.

2. STABLE RETENTION IN YOUNGER DEMOGRAPHICS:
   - Customers 'Under 30' show the lowest churn rate at 9.75% (201 churned out of 2,061 customers).
   - The '30-50' bracket maintains a moderate churn rate of 10.26% (388 churned out of 3,782 customers).

3. STRATEGIC IMPLICATION:
   - Older users are dropping off at a higher frequency, suggesting potential onboarding friction, accessibility barriers, or product complexity issues.
   - Recommendation: Conduct targeted customer feedback surveys for the 51+ demographic and streamline UI/UX and customer support touchpoints for senior users.
*/