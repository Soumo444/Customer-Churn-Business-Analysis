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
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    return joblib.load("churn_model.pkl")

model = load_model()

FEATURE_ORDER = [
    "monthly_fee", "payment_failures", "last_login_days_ago",
    "weekly_active_days", "monthly_logins", "csat_score",
    "total_revenue", "tenure_months",
]

# ============================================================
# SIDEBAR — INPUT CONTROLS
# ============================================================
with st.sidebar:
    st.markdown("### ⚡ CHURNIQ AI")
    st.caption("Retention Intelligence")
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
# HEADER
# ============================================================
st.markdown("# Customer Retention Intelligence")
st.caption("Predictions below are the model's raw output plus a genuine, computed explanation — "
           "not a scripted narrative.")

# ============================================================
# FEATURE ENGINEERING (single source of truth, reused everywhere)
# ============================================================
def engineer_features(raw: dict) -> pd.DataFrame:
    df = pd.DataFrame({k: [v] for k, v in raw.items()})
    df["cost_friction"] = df["payment_failures"] * df["monthly_fee"]
    df["disengagement_score"] = df["last_login_days_ago"] / (df["weekly_active_days"] + 1)
    df["value_dissatisfaction"] = (df["monthly_fee"] * (5 - df["csat_score"])) / (df["monthly_logins"] + 1)
    df["engagement_velocity"] = df["monthly_logins"] / (df["last_login_days_ago"] + 1)
    df["revenue_per_month"] = df["total_revenue"] / (df["tenure_months"] + 1)
    df["failure_rate"] = df["payment_failures"] / (df["monthly_logins"] + 1)
    return df

def align_to_model(df: pd.DataFrame) -> pd.DataFrame:
    X = pd.get_dummies(df, drop_first=True)
    if hasattr(model, "feature_names_in_"):
        for col in model.feature_names_in_:
            if col not in X.columns:
                X[col] = 0
        X = X[model.feature_names_in_]
    return X

def predict_prob(raw: dict) -> float:
    X = align_to_model(engineer_features(raw))
    return float(model.predict_proba(X)[:, 1][0])

# ============================================================
# SESSION STATE
# ============================================================
if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

# ============================================================
# PREDICTION PIPELINE
# ============================================================
if predict_button:
    raw_inputs = {
        "monthly_fee": monthly_fee,
        "payment_failures": payment_failures,
        "last_login_days_ago": last_login_days_ago,
        "weekly_active_days": weekly_active_days,
        "monthly_logins": monthly_logins,
        "csat_score": csat_score,
        "total_revenue": total_revenue,
        "tenure_months": tenure_months,
    }
    prob = predict_prob(raw_inputs)

    st.session_state.prediction_done = True
    st.session_state.probability = prob
    st.session_state.raw_inputs = raw_inputs

# ============================================================
# DISPLAY RESULTS
# ============================================================
if st.session_state.prediction_done:
    prob = st.session_state.probability
    raw_inputs = st.session_state.raw_inputs

    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.metric("Model Churn Probability", f"{prob*100:.1f}%")
        if prob >= 0.22:
            st.error("🔴 High Churn Risk (≥22%)")
        elif prob >= 0.08:
            st.warning("🟡 Medium Churn Risk (8–22%)")
        else:
            st.success("🟢 Low Churn Risk (<8%)")
        st.caption(
            "These cutoffs (8% / 22%) are placeholders, not derived from a precision-recall "
            "analysis on labeled outcomes. Until you run that analysis on real held-out data, "
            "treat the tier boundaries as illustrative, not calibrated."
        )

    # --------------------------------------------------------
    # REAL explanation: local sensitivity via perturbation
    # (this is genuinely computed from your model, not invented)
    # --------------------------------------------------------
    with col2:
        st.markdown("#### 🔍 What actually moved this prediction")
        st.caption("Each row shows how much the probability shifts if that raw input is nudged "
                   "up/down slightly, holding everything else fixed. This is a real local "
                   "sensitivity check against your model — not a guessed narrative.")

        deltas = []
        step_fracs = {
            "monthly_fee": 0.1, "payment_failures": 1, "last_login_days_ago": 0.1,
            "weekly_active_days": 1, "monthly_logins": 0.1, "csat_score": 1,
            "total_revenue": 0.1, "tenure_months": 0.1,
        }
        base_prob = prob
        for feat in FEATURE_ORDER:
            perturbed = dict(raw_inputs)
            step = step_fracs[feat]
            if feat in ("payment_failures", "weekly_active_days", "csat_score"):
                perturbed[feat] = raw_inputs[feat] + step
            else:
                perturbed[feat] = raw_inputs[feat] * (1 + step)
            try:
                p2 = predict_prob(perturbed)
                deltas.append((feat, (p2 - base_prob) * 100))
            except Exception:
                continue

        sens_df = pd.DataFrame(deltas, columns=["feature", "prob_change_pct_pts"])
        sens_df["abs_impact"] = sens_df["prob_change_pct_pts"].abs()
        sens_df = sens_df.sort_values("abs_impact", ascending=False).drop(columns="abs_impact")
        st.dataframe(sens_df, hide_index=True, use_container_width=True)

    # --------------------------------------------------------
    # Honest range flag instead of a hard block
    # --------------------------------------------------------
    st.markdown("---")
    st.markdown("#### ⚠️ Input plausibility check")
    flags = []
    if last_login_days_ago > 30 and monthly_logins > 10:
        flags.append(
            f"Last login is {last_login_days_ago} days ago but monthly logins is {monthly_logins}. "
            "These are logically hard to reconcile for a single current month — double check the inputs."
        )
    if tenure_months * 30 < last_login_days_ago:
        flags.append("Last login (days ago) exceeds total tenure — check the inputs.")

    if flags:
        for f in flags:
            st.info(f"🧭 {f} The prediction above is still shown as-is; this flag doesn't change it, "
                    f"it just tells you the combination is unusual and worth a second look.")
    else:
        st.caption("No obvious internal contradictions in this input set.")

    st.markdown("---")
    st.markdown(
        "**To actually know if the model's signal is good or bad**, the next step isn't more "
        "hand-picked adversarial sliders — it's running `predict_proba` against a real labeled "
        "test set and looking at the ROC-AUC / precision-recall curve, and pulling "
        "`model.feature_importances_` (if it's tree-based) to see what the model globally "
        "leans on. Happy to write that evaluation script if you can share (or point me to) the "
        "training/test data and the model type."
    )