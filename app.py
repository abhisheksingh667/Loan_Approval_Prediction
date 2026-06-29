import os 
print("Current directory:",os.getcwd())
print("Files:",os.listdir())

import streamlit as st
import joblib
import numpy as np


# model = joblib.load("../models/loan_approval_model.pkl")
# scaler = joblib.load("../models/scaler.pkl")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "models", "loan_approval_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Loan Approval Prediction")
st.write("Enter applicant details to predict loan approval.")

no_of_dependents = st.number_input("Number of Dependents", 0, 10)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

income_annum = st.number_input("Annual Income", min_value=0)

loan_amount = st.number_input("Loan Amount", min_value=0)

loan_term = st.number_input("Loan Term (Years)", min_value=1)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900
)

residential_assets = st.number_input("Residential Assets Value", min_value=0)

commercial_assets = st.number_input("Commercial Assets Value", min_value=0)

luxury_assets = st.number_input("Luxury Assets Value", min_value=0)

bank_assets = st.number_input("Bank Assets Value", min_value=0)

education = 1 if education == "Graduate" else 0

self_employed = 1 if self_employed == "Yes" else 0


total_assets = (
    residential_assets +
    commercial_assets +
    luxury_assets +
    bank_assets
)

loan_income_ratio = loan_amount / income_annum if income_annum != 0 else 0

asset_coverage_ratio = (
    total_assets / loan_amount
    if loan_amount != 0 else 0
)

if st.button("Predict"):

    features = np.array([[
        no_of_dependents,
        education,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets,
        commercial_assets,
        luxury_assets,
        bank_assets,
        total_assets,
        loan_income_ratio,
        asset_coverage_ratio
    ]])

    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
        st.write(f"Confidence: {probability[1]*100:.2f}%")
    else:
        st.error("❌ Loan Rejected")
        st.write(f"Confidence: {probability[0]*100:.2f}%")