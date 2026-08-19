import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Customer Churn Prediction App", page_icon="📊", layout="centered"
)


# Load Trained Model
@st.cache_resource
def load_model():
  # Change this from "python-analytics/churn_model.pkl" to just "churn_model.pkl"
  return joblib.load("churn_model.pkl")

model = load_model()

st.title("📊 Customer Churn Prediction & Retention Dashboard")
st.markdown(
    "Test live customer telemetry below to predict churn probability in"
    " real-time using your optimized ensemble model."
)

# Sidebar Inputs for Customer Features
st.sidebar.header("Customer Telemetry Input")

monthly_fee = st.sidebar.slider("Monthly Fee ($)", 10, 200, 50)
payment_failures = st.sidebar.number_input(
    "Payment Failures", min_value=0, max_value=10, value=0
)
last_login_days_ago = st.sidebar.slider("Last Login (Days Ago)", 0, 90, 5)
weekly_active_days = st.sidebar.slider("Weekly Active Days", 0, 7, 4)
monthly_logins = st.sidebar.number_input(
    "Monthly Logins", min_value=0, max_value=100, value=15
)
csat_score = st.sidebar.slider("CSAT Score (1-5)", 1, 5, 4)
total_revenue = st.sidebar.number_input(
    "Total Revenue ($)", min_value=0.0, value=500.0
)
tenure_months = st.sidebar.slider("Tenure (Months)", 1, 60, 12)

# Prediction Logic on Main Panel
if st.button("Predict Churn Risk", type="primary"):
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

  # Feature Engineering Pipeline
  input_data["cost_friction"] = (
      input_data["payment_failures"] * input_data["monthly_fee"]
  )
  input_data["disengagement_score"] = input_data["last_login_days_ago"] / (
      input_data["weekly_active_days"] + 1
  )
  input_data["value_dissatisfaction"] = (
      input_data["monthly_fee"] * (5 - input_data["csat_score"])
  ) / (input_data["monthly_logins"] + 1)
  input_data["engagement_velocity"] = input_data["monthly_logins"] / (
      input_data["last_login_days_ago"] + 1
  )
  input_data["revenue_per_month"] = input_data["total_revenue"] / (
      input_data["tenure_months"] + 1
  )
  input_data["failure_rate"] = input_data["payment_failures"] / (
      input_data["monthly_logins"] + 1
  )

  X_pred = pd.get_dummies(input_data, drop_first=True)

  if hasattr(model, "feature_names_in_"):
    for col in model.feature_names_in_:
      if col not in X_pred.columns:
        X_pred[col] = 0
    X_pred = X_pred[model.feature_names_in_]

  # Generate Prediction Probability (Using 0.30 threshold)
  prob = model.predict_proba(X_pred)[:, 1][0]
  prediction = (prob >= 0.30).astype(int)

  st.markdown("---")
  st.subheader("Prediction Results")

  col1, col2 = st.columns(2)
  with col1:
    st.metric(
        label="Churn Probability",
        value=f"{prob * 100:.1f}%",
        delta="High Risk" if prob >= 0.30 else "Low Risk (Loyal)",
        delta_color="inverse",
    )

  with col2:
    if prediction == 1:
      st.error(
          "🚨 **Status: HIGH CHURN RISK**\n\nImmediate retention action"
          " recommended."
      )
    else:
      st.success(
          "✅ **Status: LOYAL CUSTOMER**\n\nCustomer is stable and engaged."
      )