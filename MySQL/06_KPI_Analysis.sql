USE customer_churn_retention;

-- ==========================================
-- CUSTOMER CHURN & RETENTION KPI ANALYSIS
-- ==========================================

SELECT
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    SUM(churn = 0) AS retained_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_percentage,
    ROUND(SUM(churn = 0) * 100.0 / COUNT(*), 2) AS retention_rate_percentage,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(SUM(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END), 2) AS churned_customer_revenue,
    ROUND(SUM(CASE WHEN churn = 0 THEN total_revenue ELSE 0 END), 2) AS retained_customer_revenue,
    ROUND(AVG(total_revenue), 2) AS avg_customer_revenue,
    ROUND(AVG(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END), 2) AS avg_churned_customer_revenue,
    ROUND(AVG(CASE WHEN churn = 0 THEN total_revenue ELSE 0 END), 2) AS avg_retained_customer_revenue
FROM customer_churn_retention.customers;


