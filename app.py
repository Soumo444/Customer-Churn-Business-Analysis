import joblib
import numpy as np
import pandas as pd
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="CHURNIQ | Enterprise Retention Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# ULTRA-MODERN SAAS DESIGN SYSTEM (CSS)
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Theme Overrides */
    .stApp {
        background-color: #030712;
        color: #F3F4F6;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }
    
    section[data-testid="stSidebar"] .stMarkdown h3, 
    section[data-testid="stSidebar"] .stMarkdown h4 {
        color: #F9FAFB;
        letter-spacing: -0.025em;
    }

    /* Glassmorphic Cards */
    .glass-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.7) 0%, rgba(11, 15, 25, 0.9) 100%);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 15px 35px -10px rgba(99, 102, 241, 0.15);
    }

    .card-header {
        font-size: 14px;
        font-weight: 700;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    
    .card-subtext {
        font-size: 12px;
        color: #6B7280;
        margin-bottom: 16px;
    }

    /* Elite KPI Tiles */
    .metric-tile {
        background: rgba(17, 24, 39, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 18px;
        position: relative;
        overflow: hidden;
    }
    
    .metric-tile::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 3px; height: 100%;
        background: #6366F1;
    }

    .metric-title {
        font-size: 11px;
        font-weight: 600;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .metric-value {
        font-size: 28px;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 6px;
        letter-spacing: -0.03em;
    }

    .metric-badge {
        position: absolute;
        top: 14px;
        right: 14px;
        font-size: 10px;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 20px;
    }
    
    .badge-indigo { background: rgba(99, 102, 241, 0.15); color: #818CF8; border: 1px solid rgba(99, 102, 241, 0.3); }
    .badge-emerald { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-violet { background: rgba(139, 92, 246, 0.15); color: #C084FC; border: 1px solid rgba(139, 92, 246, 0.3); }

    /* Risk Hero Banners */
    .risk-banner-high {
        background: linear-gradient(135deg, rgba(127, 29, 29, 0.4) 0%, rgba(17, 24, 39, 0.9) 100%);
        border: 1px solid rgba(239, 68, 68, 0.4);
        border-radius: 20px;
        padding: 32px;
        text-align: center;
        box-shadow: 0 0 40px rgba(239, 68, 68, 0.15);
        height: 100%;
    }
    
    .risk-banner-med {
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.4) 0%, rgba(17, 24, 39, 0.9) 100%);
        border: 1px solid rgba(245, 158, 11, 0.4);
        border-radius: 20px;
        padding: 32px;
        text-align: center;
        box-shadow: 0 0 40px rgba(245, 158, 11, 0.15);
        height: 100%;
    }
    
    .risk-banner-low {
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.4) 0%, rgba(17, 24, 39, 0.9) 100%);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 20px;
        padding: 32px;
        text-align: center;
        box-shadow: 0 0 40px rgba(16, 185, 129, 0.15);
        height: 100%;
    }

    /* Custom Button Polish */
    .stButton button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
        color: white;
        font-weight: 600;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1rem;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #4F46E5 100%, #4338CA 100%);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
        transform: translateY(-1px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    return joblib.load("churn_model.pkl")

model = load_model()

# ============================================================
# SIDEBAR — INPUT CONTROLS
# ============================================================
with st.sidebar:
    st.markdown("### ⚡ CHURNIQ AI")
    st.caption("Advanced Retention Intelligence")
    st.markdown("---")

    st.markdown("#### 💳 Financial Metrics")
    monthly_fee = st.slider("Monthly Fee ($)", 10, 200, 50)
    total_revenue = st.number_input("Total Revenue ($)", min_value=0.0, value=500.0, step=50.0)
    payment_failures = st.number_input("Payment Failures", min_value=0, max_value=10, value=0, step=1)

    st.markdown("#### 📈 Behavioral Telemetry")
    last_login_days_ago = st.slider("Last Login (Days Ago)", 0, 90, 5)
    weekly_active_days = st.slider("Weekly Active Days", 0, 7, 4)
    monthly_logins = st.number_input("Monthly Logins", min_value=0, max_value=100, value=15, step=1)
    tenure_months = st.slider("Tenure (Months)", 1, 60, 12)

    st.markdown("#### 🌟 Experience & Feedback")
    csat_score = st.slider("CSAT Score (1-5)", 1, 5, 4)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_button = st.button("RUN PREDICTIVE ANALYSIS", use_container_width=True)

# ============================================================
# MAIN PAGE HEADER
# ============================================================
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.markdown("# Customer Retention Intelligence")
    st.markdown("<p style='color: #9CA3AF; font-size: 15px;'>Real-time AI telemetry evaluating behavioral friction, churn probability, and automated retention strategies.</p>", unsafe_allow_html=True)
with col_head2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'><span class='metric-badge badge-emerald' style='font-size: 12px; padding: 6px 12px;'>🟢 Neural Engine Online</span></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# CUSTOMER SNAPSHOT (Glassmorphic Container Grid)
# ============================================================
st.markdown(
    """
    <div class="glass-card">
        <div class="card-header">📊 Customer Snapshot Telemetry</div>
        <div class="card-subtext">Aggregated account metrics and financial profile</div>
    """,
    unsafe_allow_html=True,
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        f"""
        <div class="metric-tile">
            <span class="metric-badge badge-indigo">Active</span>
            <div class="metric-title">Monthly Fee</div>
            <div class="metric-value">${monthly_fee:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi2:
    st.markdown(
        f"""
        <div class="metric-tile">
            <span class="metric-badge badge-violet">Tenure</span>
            <div class="metric-title">Customer Age</div>
            <div class="metric-value">{tenure_months} <span style="font-size: 14px; color: #6B7280;">mos</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi3:
    st.markdown(
        f"""
        <div class="metric-tile">
            <span class="metric-badge badge-emerald">Engagement</span>
            <div class="metric-title">Monthly Logins</div>
            <div class="metric-value">{monthly_logins}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi4:
    st.markdown(
        f"""
        <div class="metric-tile">
            <span class="metric-badge badge-indigo">Rating</span>
            <div class="metric-title">CSAT Score</div>
            <div class="metric-value">{csat_score} <span style="font-size: 14px; color: #6B7280;">/ 5</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================
if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False
if "probability" not in st.session_state:
    st.session_state.probability = None

# ============================================================
# PREDICTION PIPELINE & GUARDRAILS
# ============================================================
if predict_button:
    # 🚨 LOGICAL GUARDRAILS: Prevent Garbage In, Garbage Out
    if last_login_days_ago > 30 and monthly_logins > 10:
        st.error(
            f"⚠️ **Telemetry Conflict Detected:** 'Last Login' is set to {last_login_days_ago} days ago, "
            f"but 'Monthly Logins' is set to {monthly_logins}. An inactive user cannot maintain high "
            f"monthly activity volume. Please correct these parameters."
        )
        st.stop()
        
    if (tenure_months * 30) < last_login_days_ago:
        st.error(
            "⚠️ **Timeline Conflict:** 'Last Login Days Ago' cannot exceed the total customer tenure!"
        )
        st.stop()

    input_data = pd.DataFrame({
        "monthly_fee": [monthly_fee],
        "payment_failures": [payment_failures],
        "last_login_days_ago": [last_login_days_ago],
        "weekly_active_days": [weekly_active_days],
        "monthly_logins": [monthly_logins],
        "csat_score": [csat_score],
        "total_revenue": [total_revenue],
        "tenure_months": [tenure_months],
    })

    # Feature Engineering
    input_data["cost_friction"] = input_data["payment_failures"] * input_data["monthly_fee"]
    input_data["disengagement_score"] = input_data["last_login_days_ago"] / (input_data["weekly_active_days"] + 1)
    input_data["value_dissatisfaction"] = (input_data["monthly_fee"] * (5 - input_data["csat_score"])) / (input_data["monthly_logins"] + 1)
    input_data["engagement_velocity"] = input_data["monthly_logins"] / (input_data["last_login_days_ago"] + 1)
    input_data["revenue_per_month"] = input_data["total_revenue"] / (input_data["tenure_months"] + 1)
    input_data["failure_rate"] = input_data["payment_failures"] / (input_data["monthly_logins"] + 1)

    X_pred = pd.get_dummies(input_data, drop_first=True)

    if hasattr(model, "feature_names_in_"):
        for col in model.feature_names_in_:
            if col not in X_pred.columns:
                X_pred[col] = 0
        X_pred = X_pred[model.feature_names_in_]

    prob = model.predict_proba(X_pred)[:, 1][0]
    
    st.session_state.prediction_done = True
    st.session_state.probability = float(prob)

# ============================================================
# DISPLAY RESULTS
# ============================================================
if st.session_state.prediction_done:
    prob = st.session_state.probability

    st.markdown("<br>", unsafe_allow_html=True)
    
    res_col1, res_col2 = st.columns(2)

    # Risk Hero Card (High Risk >= 22%, Medium Risk >= 8%, else Low Risk)
    with res_col1:
        if prob >= 0.22:
            st.markdown(
                f"""
                <div class="risk-banner-high">
                    <div class="card-header" style="color: #FCA5A5;">Model Churn Probability</div>
                    <div style="font-size: 64px; font-weight: 900; color: #FFFFFF; margin: 10px 0; letter-spacing: -0.04em;">{prob * 100:.1f}%</div>
                    <div style="color: #EF4444; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em;">🔴 High Churn Risk Flagged</div>
                    <div style="color: #9CA3AF; font-size: 13px; margin-top: 12px; line-height: 1.5;">Customer exhibits severe friction or disengagement indicators. Immediate intervention required.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif prob >= 0.08:
            st.markdown(
                f"""
                <div class="risk-banner-med">
                    <div class="card-header" style="color: #FCD34D;">Model Churn Probability</div>
                    <div style="font-size: 64px; font-weight: 900; color: #FFFFFF; margin: 10px 0; letter-spacing: -0.04em;">{prob * 100:.1f}%</div>
                    <div style="color: #F59E0B; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em;">🟡 Medium Churn Risk Detected</div>
                    <div style="color: #9CA3AF; font-size: 13px; margin-top: 12px; line-height: 1.5;">Customer telemetry shows emerging disengagement trends. Monitor account behavior closely.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="risk-banner-low">
                    <div class="card-header" style="color: #6EE7B7;">Model Churn Probability</div>
                    <div style="font-size: 64px; font-weight: 900; color: #FFFFFF; margin: 10px 0; letter-spacing: -0.04em;">{prob * 100:.1f}%</div>
                    <div style="color: #10B981; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em;">🟢 Low Churn Risk / Stable</div>
                    <div style="color: #9CA3AF; font-size: 13px; margin-top: 12px; line-height: 1.5;">Customer account profile appears stable and healthy. Maintain regular engagement loops.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Customer Health Telemetry Panel
    with res_col2:
        st.markdown(
            """
            <div class="glass-card" style="margin-bottom: 0px; height: 100%;">
                <div class="card-header">🩺 Health Telemetry Index</div>
                <div class="card-subtext">Composite scores derived from real-time usage variables</div>
            """,
            unsafe_allow_html=True,
        )
        
        engagement_score = min(100, int((weekly_active_days / 7) * 50 + min(monthly_logins / 30, 1) * 50))
        activity_score = max(0, min(100, int(100 - (last_login_days_ago / 90 * 100))))
        satisfaction_score = int((csat_score / 5) * 100)
        payment_score = max(0, int(100 - (payment_failures * 20)))

        st.write(f"**Engagement Index ({engagement_score}%)**")
        st.progress(engagement_score / 100)

        st.write(f"**Activity Health ({activity_score}%)**")
        st.progress(activity_score / 100)

        st.write(f"**Satisfaction Score ({satisfaction_score}%)**")
        st.progress(satisfaction_score / 100)

        st.write(f"**Payment Integrity ({payment_score}%)**")
        st.progress(payment_score / 100)

        st.markdown("</div>", unsafe_allow_html=True)

    # Actionable Strategy Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
            <div class="card-header">💡 Prescriptive Retention Strategy</div>
            <div class="card-subtext">Automated operational workflows mapped to risk output</div>
        """,
        unsafe_allow_html=True,
    )
    
    if prob >= 0.22:
        st.error(
            "**High-Priority Intervention Protocol:** Trigger an immediate customer success outreach call. "
            "Address prolonged inactivity, review potential account roadblocks, and deploy a reactivation campaign."
        )
    elif prob >= 0.08:
        st.warning(
            "**Medium-Priority Retention Protocol:** Send an automated re-engagement email sequence "
            "highlighting new product features or offering product tips to spark account usage."
        )
    else:
        st.success(
            "**Standard Retention Protocol:** Account is in a healthy operating window. "
            "Keep automated nurture sequences running and schedule routine quarterly check-ins."
        )
    st.markdown("</div>", unsafe_allow_html=True)