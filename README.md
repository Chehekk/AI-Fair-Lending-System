# AI-Fair-Lending-System
## Live Demo: https://ai-fair-lending.streamlit.app/

## Overview

AI-Fair-Lending-System is an AI-powered fintech platform prototype designed to support fair, explainable, and risk-aware lending decisions. The project uses machine learning to predict borrower risk, recommend lending strategies, detect suspicious borrowing behavior, and provide interactive analytics through a Streamlit dashboard.

The goal of the project is to improve lending accessibility while maintaining financial safety using AI-driven decision-making.

---

# Features

* AI-based borrower risk prediction
* Fraud-aware lending logic
* Dynamic loan recommendations
* Risk-based interest recommendations
* Explainable AI predictions
* Progressive trust-based lending system
* Interactive Streamlit dashboard
* Analytics dashboard with visualizations

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* Streamlit
* Matplotlib
* Joblib

---

# Machine Learning Workflow

1. Data preprocessing
2. Feature engineering
3. Random Forest model training
4. Risk probability prediction
5. Risk categorization
6. Fraud detection logic
7. Dashboard visualization

---

# Risk Categories

| Risk Level  | Description                 |
| ----------- | --------------------------- |
| Low Risk    | Safe borrower profile       |
| Medium Risk | Moderate lending risk       |
| High Risk   | High probability of default |

---

# Fraud Detection Logic

The platform identifies suspicious borrower behavior such as:

* Extremely high loan requests compared to income
* Low employment stability
* High-risk financial profiles

---

# Explainable AI

The system explains why borrowers are classified into specific risk categories.

Example reasons:

* High interest rate
* Weak credit grade
* Low employment stability
* Loan amount too high compared to income

---

# Streamlit Dashboard

The application includes:

* Loan assessment interface
* AI lending analysis
* Fraud status detection
* Trust-level recommendations
* Analytics dashboard
* Feature importance visualization
* Borrower risk distribution

---

🌟 Dataset sourced from Kaggle Lending Club Loan Dataset.



# Project Structure

```bash
AI-Fair-Lending-System/
│
├── loan_risk_prediction.ipynb
├── app.py
├── loan_risk_model.pkl
├── model_columns.pkl
├── loan.csv
├── README.md
├── requirements.txt
└── AI_Fair_Lending_Report.pdf
```
# How to Run the Project
Step 1: Install required libraries

```bash
pip install -r requirements.txt
```

# Step 2: Run the Streamlit application

```bash
py -m streamlit run app.py
```

# Step 3: Open the local URL shown in the terminal

Example:

```text
http://localhost:8501
```

---

# Future Enhancements

* XGBoost integration
* Advanced fraud detection
* Real-time banking APIs
* Mobile application deployment
* Blockchain-based identity verification

---

# Author

Developed as an AI and fintech project focused on fair lending, explainable AI, and intelligent risk assessment.
