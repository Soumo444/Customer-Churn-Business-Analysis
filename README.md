# 📊 Customer Churn Business Analysis Project

An end-to-end customer churn analysis solution — from raw data collection through cleaning, exploratory analysis, database engineering, predictive modeling, and interactive dashboarding. Built to help business stakeholders understand **why customers leave** and **who is likely to leave next**.

---

## 🚀 Overview

This project delivers a complete churn analytics pipeline that combines **SQL-based data engineering**, **Python-driven analytics and machine learning**, and **Power BI visualization** into a single, cohesive workflow — turning raw customer data into actionable business insight.

---

## 🗂️ Project Structure

```
├── DATA COLLECTION/           # Raw datasets used for the analysis
├── EXCEL DATA PROFILING/      # Initial data quality checks and profiling
├── MYSQL/                     # Database scripts (setup → analysis)
│   ├── 01_DATABASE_SETUP.sql
│   ├── 02_Table_Creation.sql
│   ├── 03_Data_Import.sql
│   ├── 04_Data_Quality_Audit.sql
│   ├── 06_KPI_Analysis.sql
│   ├── 07_...
│   ├── 08_...
│   └── 09_Root_Cause_Analysis.sql
├── POWERBI_DASHBOARD/         # Power BI project file (.pbix)
├── python-analytics/          # Python analysis & modeling
│   ├── 01_mysql_connection.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Root_Cause_Analysis.ipynb
│   ├── 04_Machine_Learning_Model.ipynb
│   └── churn_model.pkl
├── app.py                     # Application script
└── requirements.txt           # Python dependencies
```

---

## 🧩 Module Breakdown

### 🗄️ MYSQL — Data Engineering
| Script | Purpose |
|---|---|
| `01_DATABASE_SETUP.sql` | Initializes the database |
| `02_Table_Creation.sql` | Defines the schema |
| `03_Data_Import.sql` | Imports processed data |
| `04_Data_Quality_Audit.sql` | Ensures data integrity |
| `06_KPI_Analysis.sql` → `09_Root_Cause_Analysis.sql` | Business intelligence and churn driver queries |

### 🐍 python-analytics — Analysis & Modeling
| Notebook | Purpose |
|---|---|
| `01_mysql_connection.ipynb` | Connects to the MySQL database |
| `02_Exploratory_Data_Analysis.ipynb` | Visualizes trends and patterns |
| `03_Root_Cause_Analysis.ipynb` | Identifies key churn drivers |
| `04_Machine_Learning_Model.ipynb` | Trains and evaluates the churn prediction model |
| `churn_model.pkl` | Saved, ready-to-use ML model |

### 📈 POWERBI_DASHBOARD
Interactive `.pbix` dashboard designed for business stakeholders to explore churn KPIs, trends, and segments visually.

---

## ✨ Key Features

- 🛠️ **Data Engineering** — Robust SQL pipelines for cleaning, structuring, and preparing raw data
- 🔍 **Exploratory Data Analysis (EDA)** — In-depth Python analysis to uncover churn drivers
- 🤖 **Predictive Modeling** — Machine learning model to forecast future customer churn
- 📊 **Dashboarding** — Interactive Power BI dashboard for real-time business insight

---

## ⚙️ Getting Started

### 1. Database Setup
Ensure MySQL is running, then execute the scripts in the `MYSQL/` folder in order to set up the database and import the data.

### 2. Environment Setup
Install all required Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Analysis
Launch and run the notebooks in `python-analytics/` in sequence to explore the data, uncover churn drivers, and train the predictive model.

---

## 🧰 Tech Stack

`MySQL` · `Python` (Pandas, Scikit-learn, Jupyter) · `Power BI` · `SQL`

---

## 📌 Notes

- Run the SQL scripts sequentially — each stage builds on the previous one.
- Notebooks should also be run in numerical order for a smooth workflow, from database connection through to model training.

---

<p align="center"><i>Built for data-driven decision making around customer retention.</i></p>
