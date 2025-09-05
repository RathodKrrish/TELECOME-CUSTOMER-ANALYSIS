# 📊 Telecom Customer Churn Analysis  

This project focuses on analyzing **customer churn in the telecom sector** using **Python, SQL, and Power BI**. It delivers a complete pipeline: data ingestion → cleaning → analysis → predictive modeling → interactive dashboard, enabling businesses to uncover why customers leave and how to retain them.  

---

## 🧩 Problem Statement  
Customer churn is one of the biggest challenges in the telecom industry. Retaining existing customers is far cheaper than acquiring new ones. The goal of this project is to:  

- Identify **which customers are at risk of churn**.  
- Understand **key factors that drive churn**.  
- Provide **data-driven insights** to support proactive retention strategies.  

---

## ✅ What I Solved  
- Automated ingestion of CSV datasets into an **SQLite database** using Python (`ingestionDB.py`).  
- Performed **data preprocessing, cleaning, and transformation** on the churn dataset.  
- Conducted **Exploratory Data Analysis (EDA)** to detect churn patterns.  
- Built **ML models** to predict churn-prone customers with high accuracy.  
- Designed a **Power BI dashboard** to present KPIs and actionable insights for decision-makers.  

---

## 🔍 Insights & Outcomes  
- 📉 **26.5% of customers churned**, showing a critical business concern.  
- 👵 **Senior citizens** exhibit higher churn probability.  
- 📆 **Month-to-month contract customers** are the most likely to churn.  
- 💳 **Electronic check payment users** show the highest churn rates.  
- ⏳ Longer-tenure customers are significantly less likely to churn.  
- 📡 Customers with bundled services (internet, streaming) are more loyal.  
- 🔮 Predictive ML model achieved **~80–85% accuracy** in identifying at-risk customers.  

---

## 🛠️ Tech Stack  
- **Programming:** Python (pandas, numpy, matplotlib, seaborn, scikit-learn)  
- **Database:** SQLite (SQLAlchemy for ingestion)  
- **Visualization:** Power BI, Matplotlib, Seaborn  
- **Tools:** Jupyter Notebook  

---

## 📂 Repository Structure  
📦 TELECOME-CUSTOMER-ANALYSIS
┣ 📜 ingestionDB.py # Script to load CSVs into SQLite
┣ 📜 main.ipynb # End-to-end churn analysis notebook
┣ 📜 Telco.ipynb # Additional churn-focused notebook
┣ 📜 Telco_Customer_Churn_Dataset.csv # Dataset
┣ 📜 SKS_dashbording.pbix # Power BI interactive dashboard
┗ 📜 Dashboard design.mhtml # Dashboard design reference

yaml
Copy code

---

## 📊 Dashboard Highlights  
The **Power BI dashboard** provides:  
- 📈 Churn distribution across customer demographics & services  
- 💰 Revenue impact of churn  
- 🔑 Key retention drivers  
- 🧭 Interactive filters for deeper exploration  

---

## ▶️ How to Run  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/RathodKrrish/TELECOME-CUSTOMER-ANALYSIS.git
   cd TELECOME-CUSTOMER-ANALYSIS
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the ingestion script

bash
Copy code
python ingestionDB.py
Open Jupyter notebooks

main.ipynb → Complete analysis workflow

Telco.ipynb → Additional churn modeling

Explore the Power BI Dashboard
Open SKS_dashbording.pbix in Power BI to interact with visual insights.

🎯 Future Scope
Deploy ML model as an API for real-time churn prediction.

Connect Power BI to a live database for continuous monitoring.

Explore deep learning for advanced churn prediction.

Integrate customer segmentation for targeted retention campaigns.

👨‍💻 Author
Krish Rathod
📫 Connect: LinkedIn | GitHub
## 📂 Repository Structure
