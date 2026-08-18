# Customer Churn Business Analysis Project

This project provides an end-to-end analysis of customer churn, covering data collection, cleaning, exploratory data analysis (EDA), database management, and dashboard creation[cite: 1].

## Project Structure

- **DATA COLLECTION**: Raw datasets used for the analysis[cite: 1].
- **EXCEL DATA PROFILING**: Initial data quality checks and profiling[cite: 1].
- **MYSQL**: Database scripts for setup, table creation, data importing, quality auditing, and analysis[cite: 1]:
    - `01_DATABASE_SETUP.sql`: Database initialization[cite: 1].
    - `02_Table_Creation.sql`: Schema definition[cite: 1].
    - `03_Data_Import.sql`: Importing processed data[cite: 1].
    - `04_Data_Quality_Audit.sql`: Ensuring data integrity[cite: 1].
    - `06_KPI_Analysis.sql` to `09_Root_Cause_Analysis.sql`: SQL scripts for business intelligence[cite: 1].
- **POWERBI_DASHBOARD**: Contains the Power BI project file (`.pbix`) for visualization[cite: 1].
- **python-analytics**: Python-based analysis and modeling[cite: 1]:
    - `01_mysql_connection.ipynb`: Establishing connection to MySQL[cite: 1].
    - `02_Exploratory_Data_Analysis.ipynb`: Data visualization and insights[cite: 1].
    - `03_Root_Cause_Analysis.ipynb`: Finding churn drivers[cite: 1].
    - `04_Machine_Learning_Model.ipynb`: Predicting customer churn[cite: 1].
    - `churn_model.pkl`: Saved machine learning model[cite: 1].
- **app.py**: Application script[cite: 1].
- **requirements.txt**: List of Python dependencies[cite: 1].

## Key Features
- **Data Engineering**: Robust SQL pipelines for data cleaning and preparation[cite: 1].
- **Exploratory Data Analysis (EDA)**: Comprehensive Python analysis to understand churn drivers[cite: 1].
- **Predictive Modeling**: Machine learning implementation to forecast future churn[cite: 1].
- **Dashboarding**: Interactive Power BI dashboard for business stakeholders[cite: 1].

## Getting Started
1. **Database Setup**: Ensure MySQL is running. Use the scripts in the `MYSQL` folder to set up the database and import data[cite: 1].
2. **Environment**: Install dependencies: `pip install -r requirements.txt`[cite: 1].
3. **Analytics**: Run the Jupyter notebooks in `python-analytics` to explore data and train models[cite: 1].