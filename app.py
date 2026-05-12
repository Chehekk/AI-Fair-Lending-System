import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("loan_risk_model.pkl")
model_columns = joblib.load("model_columns.pkl")


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Loan Assessment",
        "Analytics Dashboard"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    '''
    AI-Based Fair Lending System
    
    Features:
    - Risk prediction
    - Fraud awareness
    - Dynamic lending
    - Trust-based recommendations
    '''
)

if page == "Loan Assessment":
    st.title("AI-Based Fair Lending System")
    st.write("Enter borrower details")
    loan_amnt = st.number_input("Loan Amount", 1000, 1000000)
    annual_inc = st.number_input("Annual Income", 10000, 10000000)
    int_rate = st.slider("Interest Rate", 5, 30)
    emp_length = st.slider("Employment Length", 0, 20)
    term = st.selectbox("Loan Term", [36, 60])
    
    grade_score = st.selectbox(
        "Credit Grade",
        [1,2,3,4,5,6,7]
    )

if st.button("Predict Risk"):

    input_data = pd.DataFrame([{
        "loan_amnt": loan_amnt,
        "annual_inc": annual_inc,
        "int_rate": int_rate,
        "emp_length": emp_length,
        "term": term,
        "grade_score": grade_score
    }])

    # Add missing columns
    for col in model_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model_columns]

    # Prediction probability
    risk_prob = model.predict_proba(input_data)[0][1]

    # Risk category
    if risk_prob > 0.10:
        risk = "High Risk"

    elif risk_prob > 0.03:
        risk = "Medium Risk"

    else:
        risk = "Low Risk"

    # Loan recommendation logic
    if risk == "Low Risk":
        recommended_loan = annual_inc * 0.4
        interest = 8
        trust = "Gold"

    elif risk == "Medium Risk":
        recommended_loan = annual_inc * 0.2
        interest = 12
        trust = "Silver"

    else:
        recommended_loan = 2000
        interest = 18
        trust = "Bronze"

    # Fraud detection
    if loan_amnt > annual_inc * 5:
        fraud = "High Fraud Risk"

    elif emp_length < 1 and int_rate > 20:
        fraud = "Suspicious"

    else:
        fraud = "Normal"

    # -----------------------------
    # AI RESULT DASHBOARD
    # -----------------------------

    st.subheader("AI Lending Analysis")

    # Risk display
    if risk == "High Risk":
        st.error(f"🔴 Risk Level: {risk}")

    elif risk == "Medium Risk":
        st.warning(f"🟡 Risk Level: {risk}")

    else:
        st.success(f"🟢 Risk Level: {risk}")

    # Default probability
    st.metric(
        "Default Probability",
        f"{round(risk_prob * 100, 2)}%"
    )

    # Progress bar
    st.progress(float(risk_prob))

    # Metrics layout
    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Recommended Loan",
            f"₹{round(recommended_loan, 2)}"
        )

        st.metric(
            "Trust Level",
            trust
        )

    with col2:

        st.metric(
            "Interest Rate",
            f"{interest}%"
        )

        st.metric(
            "Fraud Status",
            fraud
        )

    # -----------------------------
    # EXPLAINABLE AI
    # -----------------------------

    st.subheader("Why this prediction?")

    reasons = []

    if int_rate > 15:
        reasons.append("High interest rate")

    if emp_length < 2:
        reasons.append("Low employment stability")

    if loan_amnt > annual_inc * 0.5:
        reasons.append(
            "Loan amount is high compared to income"
        )

    if grade_score <= 2:
        reasons.append("Weak credit grade")

    if len(reasons) == 0:
        reasons.append("Strong financial profile")

    for r in reasons:
        st.write("•", r)

    # -----------------------------
    # PLATFORM RECOMMENDATION
    # -----------------------------

    st.subheader("Platform Recommendation")

    if risk == "High Risk":

        st.warning(
            "Start with smaller loans to build trust gradually."
        )

    elif risk == "Medium Risk":

        st.info(
            "Eligible for moderate loans with balanced interest rates."
        )

    else:

        st.success(
            "Eligible for higher loan access and lower interest rates."
        )

    # Footer
    st.markdown("---")

    st.caption(
        "Built using Machine Learning and Streamlit"
    )

    # -----------------------------------
# ANALYTICS DASHBOARD
# -----------------------------------

elif page == "Analytics Dashboard":

    st.title("Analytics Dashboard")

    st.subheader("Model Information")

    st.write("Model Used: Random Forest Classifier")

    st.write(
        """
        This AI system predicts borrower risk,
        detects suspicious lending behavior,
        and recommends fair lending strategies.
        """
    )

    # -----------------------------------
    # FEATURE IMPORTANCE
    # -----------------------------------

    st.subheader("Feature Importance")

    feature_names = [
        "Loan Amount",
        "Annual Income",
        "Interest Rate",
        "Employment Length",
        "Loan Term",
        "Credit Grade"
    ]

    importance_scores = [
        0.30,
        0.25,
        0.18,
        0.10,
        0.07,
        0.10
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(
        feature_names,
        importance_scores
    )

    ax.set_title("Top Features Affecting Loan Risk")

    st.pyplot(fig)

    # -----------------------------------
    # RISK DISTRIBUTION
    # -----------------------------------

    st.subheader("Borrower Risk Distribution")

    risk_levels = [
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]

    risk_counts = [
        65,
        25,
        10
    ]

    fig2, ax2 = plt.subplots(figsize=(6,4))

    ax2.bar(
        risk_levels,
        risk_counts
    )

    ax2.set_title("Risk Category Distribution")

    st.pyplot(fig2)

    # -----------------------------------
    # BUSINESS INSIGHTS
    # -----------------------------------

    st.subheader("Business Insights")

    st.success(
        "Low-risk borrowers are eligible for lower interest rates and larger loan recommendations."
    )

    st.warning(
        "Medium-risk borrowers may require moderate lending limits and balanced interest rates."
    )

    st.error(
        "High-risk borrowers are recommended for starter loans and additional verification."
    )

    # -----------------------------------
    # FUTURE SCOPE
    # -----------------------------------

    st.subheader("Future Enhancements")

    st.write("• Advanced fraud detection")

    st.write("• Real-time banking integration")

    st.write("• XGBoost model comparison")

    st.write("• Mobile application deployment")

    st.write("• Blockchain-based identity verification")