USE customer_churn_retention;

-- Check total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Check duplicate customer IDs
SELECT customer_id, COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Check missing customer IDs
SELECT COUNT(*) AS missing_customer_id
FROM customers
WHERE customer_id IS NULL;

-- ==========================================
-- Additional Data Quality Checks
-- ==========================================

-- 4. Check missing values in all important columns
SELECT
    SUM(gender IS NULL) AS missing_gender,
    SUM(age IS NULL) AS missing_age,
    SUM(country IS NULL) AS missing_country,
    SUM(city IS NULL) AS missing_city,
    SUM(customer_segment IS NULL) AS missing_segment,
    SUM(tenure_months IS NULL) AS missing_tenure,
    SUM(signup_channel IS NULL) AS missing_signup_channel,
    SUM(contract_type IS NULL) AS missing_contract_type,
    SUM(monthly_logins IS NULL) AS missing_logins,
    SUM(weekly_active_days IS NULL) AS missing_active_days,
    SUM(avg_session_time IS NULL) AS missing_session_time,
    SUM(features_used IS NULL) AS missing_features,
    SUM(usage_growth_rate IS NULL) AS missing_growth_rate,
    SUM(last_login_days_ago IS NULL) AS missing_last_login,
    SUM(monthly_fee IS NULL) AS missing_fee,
    SUM(total_revenue IS NULL) AS missing_revenue,
    SUM(payment_method IS NULL) AS missing_payment_method,
    SUM(payment_failures IS NULL) AS missing_payment_failures,
    SUM(support_tickets IS NULL) AS missing_support_tickets,
    SUM(csat_score IS NULL) AS missing_csat,
    SUM(nps_score IS NULL) AS missing_nps,
    SUM(churn IS NULL) AS missing_churn
FROM customers;


-- 5. Check churn values
SELECT
    churn,
    COUNT(*) AS customer_count
FROM customers
GROUP BY churn
ORDER BY churn;


-- 6. Check invalid ages
SELECT COUNT(*) AS invalid_age_count
FROM customers
WHERE age < 18 OR age > 100;


-- 7. Check invalid tenure
SELECT COUNT(*) AS invalid_tenure_count
FROM customers
WHERE tenure_months < 0;


-- 8. Check invalid monthly fees
SELECT COUNT(*) AS invalid_fee_count
FROM customers
WHERE monthly_fee < 0;


-- 9. Check invalid revenue
SELECT COUNT(*) AS invalid_revenue_count
FROM customers
WHERE total_revenue < 0;


-- 10. Check invalid weekly active days
SELECT COUNT(*) AS invalid_active_days
FROM customers
WHERE weekly_active_days < 0
   OR weekly_active_days > 7;