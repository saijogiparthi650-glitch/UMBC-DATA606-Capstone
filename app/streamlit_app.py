import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# LOAD MODEL
model = joblib.load("xgboost_model.pkl")

# TITLE
st.title("💳 Credit Default Prediction App")
st.subheader("Enter customer details to predict default risk")
st.markdown("---")

# INPUTS
LIMIT_BAL = st.number_input("Credit Limit", min_value=0)

SEX = st.selectbox("Gender", [1, 2],
                    format_func=lambda x: "Male" if x == 1 else "Female")

EDUCATION = st.selectbox("Education", [1,2,3,4],
                        format_func=lambda x: ["Graduate","University","High School","Others"][x-1])

MARRIAGE = st.selectbox("Marriage", [1,2,3],
                        format_func=lambda x: ["Married","Single","Others"][x-1])

AGE = st.number_input("Age", min_value=18, max_value=100)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("## Payment History")
    PAY_0 = st.number_input("Repayment Status (Last Month)")
    PAY_2 = st.number_input("Repayment Status (2 Months Ago)")
    PAY_3 = st.number_input("Repayment Status (3 Months Ago)")
    PAY_4 = st.number_input("Repayment Status (4 Months Ago)")
    PAY_5 = st.number_input("Repayment Status (5 Months Ago)")
    PAY_6 = st.number_input("Repayment Status (6 Months Ago)")

with col2:
    st.markdown("## Billing Amount")
    BILL_AMT1 = st.number_input("Bill Amount 1")
    BILL_AMT2 = st.number_input("Bill Amount 2")
    BILL_AMT3 = st.number_input("Bill Amount 3")
    BILL_AMT4 = st.number_input("Bill Amount 4")
    BILL_AMT5 = st.number_input("Bill Amount 5")
    BILL_AMT6 = st.number_input("Bill Amount 6")

with col3:
    st.markdown("## Payment Amount")
    PAY_AMT1 = st.number_input("Payment Amount 1")
    PAY_AMT2 = st.number_input("Payment Amount 2")
    PAY_AMT3 = st.number_input("Payment Amount 3")
    PAY_AMT4 = st.number_input("Payment Amount 4")
    PAY_AMT5 = st.number_input("Payment Amount 5")
    PAY_AMT6 = st.number_input("Payment Amount 6")

st.markdown("---")

# BUTTON STYLE
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 20px;
    font-weight: bold;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# PREDICTION BUTTON
if st.button("🚀 Predict Default Risk"):

    input_data = np.array([[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
                            PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                            BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                            PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    risk_score = probability[0][1]

    st.markdown("---")

    # TEXT OUTPUT
    if prediction[0] == 1:
        st.error(f"⚠️ High Risk of Default\n\nProbability: {risk_score:.2f}")
    else:
        st.success(f"✅ Low Risk\n\nProbability: {risk_score:.2f}")

    # RISK CATEGORY 
    if risk_score < 0.3:
        risk_label = "Low Risk"
        color = "green"
    elif risk_score < 0.7:
        risk_label = "Moderate Risk"
        color = "yellow"
    else:
        risk_label = "High Risk"
        color = "red"

    # GAUGE CHART 
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score * 100,
        title={'text': f"Risk Level: {risk_label}"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "khaki"},
                {'range': [70, 100], 'color': "lightcoral"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # INTERPRETATION 
    st.markdown(f"""
    ### 📊 Interpretation:
    - **Risk Score:** {risk_score:.2f}
    - **Category:** {risk_label}

    💡 Customers in this range typically have a **{risk_label.lower()} likelihood of default**.
    """)