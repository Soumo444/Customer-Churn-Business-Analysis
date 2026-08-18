-- ==============================================================================
-- 1. ROOT CAUSE: CHURN & REVENUE LOSS BY TENURE BRACKETS
-- PURPOSE: Find if customers leave early (Onboarding Failure) or late (Product Burnout)
-- ==============================================================================
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
GROUP BY tenure_group
ORDER BY lost_revenue DESC;


/* 
BUSINESS INSIGHTS & ROOT CAUSE FINDINGS (TENURE):

1. PRIMARY ROOT CAUSE - ONBOARDING DROP-OFF:
   - New customers (0-6 Months) experience a massive 28.10% churn rate (290 churned out of 1,032 new signups).
   - Verdict: The business has a severe early customer activation and product adoption issue.

2. LONG-TERM RETENTION IS STRONG:
   - Customers who survive past 6 months become highly loyal, with churn dropping to ~8.8% for 6-24 months and 7.83% for 2+ years.
   
3. FINANCIAL EXPOSURE:
   - Churn among 2+ year customers accounts for $683,490.00 in lost historical revenue due to accumulated customer value over time.

4. ACTIONABLE RECOMMENDATIONS:
   - Redesign the 0-90 day customer onboarding sequence (welcome emails, walkthrough tutorials, dedicated support check-ins).
   - Implement early-warning activity alerts to flag new users who aren't engaging within their first 30 days.
*/

-- ==============================================================================
-- 2. ROOT CAUSE: CHURN & REVENUE LOSS BY SIGNUP CHANNEL
-- PURPOSE: Identify which marketing/acquisition channels bring high vs. low quality users
-- ==============================================================================
SELECT 
    signup_channel,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(SUM(churn) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN churn = 1 THEN total_revenue ELSE 0 END), 2) AS lost_revenue
FROM customer_churn_retention.customers
GROUP BY signup_channel
ORDER BY lost_revenue DESC;

/* 
BUSINESS INSIGHTS & ROOT CAUSE FINDINGS (SIGNUP CHANNEL):

1. WEB ACQUISITION DRIVES HIGHEST ABSOLUTE LOSS:
   - Web signups represent over half of all customers (5,036) and account for the largest financial loss ($420,790.00 lost revenue across 501 churned users).

2. REFERRAL PROGRAM SURPRISE:
   - Referral signups exhibit a slightly higher churn rate (11.18%) compared to Web (9.95%) and Mobile (10.00%).
   - Takeaway: Word-of-mouth or incentivized referral channels are not guaranteeing higher customer loyalty in this dataset.

3. BALANCED CHANNEL DISTRIBUTION:
   - Churn percentages are fairly consistent across acquisition channels (~10%–11%), reinforcing that early-stage product onboarding (0–6 months) is the primary churn driver rather than channel-specific lead quality.
*/
