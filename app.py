import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    customer_churn_risk_model.pkl"
)

st.set_page_config(
    page_title="AI Customer Churn Risk Assessment",
    layout="centered"
)

st.title("AI Customer Churn Risk Assessment")


st.write(
    "This application estimates the likelihood that a customer may leave the company based on customer account information."
)

st.divider()


tenure = st.number_input(
    "Customer Tenure (Months)",
    min_value=0,
    max_value=100,
    value=12
)


MonthlyCharges	 = st.number_input(
    "Customer Monthly Charges (Months)  ($)",
    min_value=0,
    max_value=100,
    value=50
)



Contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)



InternetService = st.selectbox(
    "InternetService Type",
    ["Fiber optic", "DSL", "No"]
)


TechSupport	  = st.selectbox(
    "TechSupport ",
    ["Yes ", "No internet service", "No"]
)


OnlineSecurity = st.selectbox(
    "OnlineSecurity ",
    ["Yes ", "No internet service", "No"]
)

if st.button("prediction"):
    input_data = pd.DataFrame(
    [[tenure, MonthlyCharges , Contract,  
    InternetService, TechSupport, 
    OnlineSecurity]],
    columns = ["tenure", "MonthlyCharges", "Contract", "InternetService", "TechSupport", "OnlineSecurity" ])

    input_data = pd.get_dummies(input_data)

    input_data = input_data.reindex(
    columns=model.feature_names_in_,
    fill_value=0
)




    st.subheader("Assesment Result")

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Higher churn risk")
        st.caption("This assessment is based on historical customer behavior patterns.")
        
    else:
        st.success("lower churn ris")
        st.caption("This assessment is based on historical customer behavior patterns.")
    





