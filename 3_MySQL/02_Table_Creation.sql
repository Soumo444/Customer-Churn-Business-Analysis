CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    gender VARCHAR(20),
    age INT,
    country VARCHAR(50),
    city VARCHAR(50),
    customer_segment VARCHAR(30),
    tenure_months INT,
    signup_channel VARCHAR(30),
    contract_type VARCHAR(30),
    monthly_logins INT,
    weekly_active_days INT,
    avg_session_time DECIMAL(10,2),
    features_used INT,
    usage_growth_rate DECIMAL(10,2),
    last_login_days_ago INT,
    monthly_fee DECIMAL(10,2),
    total_revenue DECIMAL(12,2),
    payment_method VARCHAR(30),
    payment_failures INT,
    discount_applied VARCHAR(10),
    price_increase_last_3m VARCHAR(10),
    support_tickets INT,
    avg_resolution_time DECIMAL(10,2),
    complaint_type VARCHAR(50),
    csat_score INT,
    escalations INT,
    email_open_rate DECIMAL(10,2),
    marketing_click_rate DECIMAL(10,2),
    nps_score INT,
    survey_response VARCHAR(30),
    referral_count INT,
    churn TINYINT
);

DESCRIBE customers;


SELECT COUNT(*) AS total_columns
FROM information_schema.columns
WHERE table_schema = 'customer_churn_retention'
AND table_name = 'customers';