USE customer_churn_retention;

-- ==============================================================================
-- VIEW 1: EXECUTIVE KPI SUMMARY
-- PURPOSE: High-level metrics (Total Customers, Churn Rate, Total Revenue, Lost Revenue)
-- ==============================================================================
CREATE OR REPLACE VIEW vw_executive_kpis AS
SELECT
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    SUM(churn = 0) AS retained_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(SUM(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END), 2) AS lost_revenue
FROM customer_churn_retention.customers;




-- ==============================================================================
-- VIEW 2: TENURE & ONBOARDING RISK SUMMARY
-- PURPOSE: Packages the main root-cause finding (0-6 Months Onboarding Drop-off)
-- ==============================================================================
CREATE OR REPLACE VIEW vw_tenure_churn_risk AS
SELECT 
    CASE 
        WHEN tenure_months <= 6 THEN '0-6 Months (New)'
        WHEN tenure_months <= 12 THEN '6-12 Months (Early)'
        WHEN tenure_months <= 24 THEN '1-2 Years (Mid-stage)'
        ELSE '2+ Years (Loyal)'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END), 2) AS lost_revenue
FROM customer_churn_retention.customers
GROUP BY tenure_group;


-- ==============================================================================
-- VIEW 3: CUSTOMER SEGMENTATION SUMMARY
-- PURPOSE: Combines Contract, Channel, and Active Days for dashboard filters
-- ==============================================================================
CREATE OR REPLACE VIEW vw_customer_segment_summary AS
SELECT 
    contract_type,
    country,
    signup_channel,
    weekly_active_days,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(total_revenue), 2) AS total_revenue
FROM customer_churn_retention.customers
GROUP BY contract_type, country, signup_channel, weekly_active_days;






-- 1. Check Executive KPIs View
SELECT * FROM vw_executive_kpis;

-- 2. Check Tenure Risk View
SELECT * FROM vw_tenure_churn_risk;

-- 3. Check Customer Segmentation View
SELECT * FROM vw_customer_segment_summary LIMIT 10;