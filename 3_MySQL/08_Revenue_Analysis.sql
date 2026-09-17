USE customer_churn_retention;

-- ==============================================================================
-- 1. AVERAGE REVENUE PER USER (ARPU) BY CHURN STATUS
-- ==============================================================================
SELECT 
    churn,
    CASE WHEN churn = 1 THEN 'Churned' ELSE 'Retained' END AS customer_status,
    COUNT(*) AS total_customers,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(AVG(total_revenue), 2) AS arpu
FROM customer_churn_retention.customers
GROUP BY churn;

/* 
BUSINESS INSIGHTS (ARPU & REVENUE METRICS):
- Total Financial Impact: Churned customers account for $862,640.00 in lost revenue across 1,021 users.
- ARPU Differential: Retained customers have an ARPU of $1,081.14, whereas churned customers averaged $844.90 prior to leaving.
- Takeaway: Lower lifetime value before churn indicates early drop-off before customers reach full account tenure.
*/


-- ==============================================================================
-- 2. REVENUE AT RISK BY CONTRACT TYPE
-- ==============================================================================
SELECT 
    contract_type,
    ROUND(SUM(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END), 2) AS lost_revenue,
    ROUND(SUM(CASE WHEN churn = 0 THEN total_revenue ELSE 0 END), 2) AS retained_revenue,
    ROUND(SUM(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END) * 100.0 / SUM(total_revenue), 2) AS lost_revenue_pct
FROM customer_churn_retention.customers
GROUP BY contract_type
ORDER BY lost_revenue DESC;

/* 
BUSINESS INSIGHTS (REVENUE AT RISK):
- Top Monetary Exposure: Monthly contracts represent the largest revenue loss ($449,970.00, accounting for 8.59% of monthly revenue).
- Substantial Contract Losses: Quarterly ($239,380.00 lost) and Yearly ($173,290.00 lost) contracts experience similar percentage losses (~7.4% - 8.2%).
- Strategy: Prioritize monthly retention workflows as saving monthly subscribers yields the highest immediate financial recovery.
*/