# 📊 Customer Churn Business Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.61.1-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Scikit--Learn-1.7.2-orange?style=for-the-badge&logo=scikit-learn" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/XGBoost-Enabled-green?style=for-the-badge" alt="XGBoost">
</p>

---

## 🎯 Project Overview
This project provides a comprehensive end-to-end business analysis of **Customer Churn**. It covers everything from raw data collection and cleaning to advanced exploratory data analysis (EDA), root cause analysis, and finally, a machine learning predictive model deployed as an interactive dashboard.

## 🚀 Key Features
*   **Data Pipeline:** Automated data collection and cleaning from raw sources.
*   **Deep Analytics:** SQL-driven KPI, Revenue, and Churn analysis.
*   **Predictive Modeling:** High-accuracy churn prediction using Machine Learning (XGBoost & RandomForest).
*   **Interactive Dashboard:** Real-time customer churn insights via **Streamlit**.

---

## 📂 Project Structure
```text
CUSTOMER_CHURN_BUSINESS_ANALYSIS/
├── .devcontainer/
│   └── devcontainer.json
├── 1_DATA_COLLECTION/
│   └── customer_churn_raw.csv
├── 2_EXCEL_DATA_PROFILING/
│   └── Data_Profiling.xlsx
├── 3_MySQL/
│   ├── 01_DATABASE_SETUP.SQL
│   ├── 02_Table_Creation.sql
│   ├── 03_Data_Import.sql
│   ├── 04_Data_Quality_Audit.sql
│   ├── 06_KPI_Analysis.sql
│   ├── 07_Churn_Analysis.sql
│   ├── 08_Revenue_Analysis.sql
│   ├── 09_Root_Cause_Analysis.sql
│   └── 10_Views.sql
├── 4_python-analytics/
│   ├── plots/
│   ├── 01_mysql_connection.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Root_Cause_Analysis.ipynb
│   └── 04_Machine_Learning_Model.ipynb
├── 5_POWERBI_DASHBOARD/
│   └── CUSTOMER_CHURN_ANALYSIS - Dashboard.pbix
├── app.py                  # 🚀 Main Streamlit app (used in production)
├── app_backup.py           # 🗄️ Local backup copy (not used by the web app)
├── churn_model.pkl
├── README.md
├── requirements.txt
└── runtime.txt
```

> 📝 **Note:** `app_backup.py` is a simple backup copy of the main application kept for safekeeping. It is **not** used or deployed by the live Streamlit web interface — only `app.py` powers the app.

## 📈 Tech Stack
*   **Language:** Python 3.11
*   **ML Library:** Scikit-learn, XGBoost
*   **Dashboard:** Streamlit
*   **Database:** MySQL
*   **Visualization:** PowerBI, Seaborn, Matplotlib

## 🌐 Live Application
Experience the dashboard here:
👉 **[Click to Open Customer Churn Dashboard](https://customer-churn-business-analysis-vtb7gvwpkvhdrtjpddnz62.streamlit.app/)**

---

## 🛠 Setup Instructions
To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Soumo444/Customer-Churn-Business-Analysis.git
   ```
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---
*Created by [Soumo444](https://github.com/Soumo444)*
