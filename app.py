import streamlit as st
import pickle
import numpy as np

# Load model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="Heart Disease Detection",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Detection System")
st.write("Enter patient details to predict heart disease risk.")

# Inputs
age = st.number_input("Age", 1, 120, 45)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ]
)

cp_map = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}
cp = cp_map[cp]

trestbps = st.number_input("Resting Blood Pressure", 80, 250, 120)

chol = st.number_input("Cholesterol", 100, 600, 200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox(
    "Resting ECG",
    [
        "Normal",
        "ST-T Wave Abnormality",
        "Left Ventricular Hypertrophy"
    ]
)

restecg_map = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
restecg = restecg_map[restecg]

thalach = st.number_input("Maximum Heart Rate Achieved", 50, 250, 150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)

slope = st.selectbox(
    "Slope",
    [
        "Upsloping",
        "Flat",
        "Downsloping"
    ]
)

slope_map = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}
slope = slope_map[slope]

ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])

thal = st.selectbox(
    "Thalassemia",
    [
        "Normal",
        "Fixed Defect",
        "Reversible Defect",
        "Unknown"
    ]
)

thal_map = {
    "Normal": 0,
    "Fixed Defect": 1,
    "Reversible Defect": 2,
    "Unknown": 3
}
thal = thal_map[thal]

# Prediction
if st.button("Predict"):
    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Heart Disease Detected")
        st.write(f"Risk Probability: {probability[1] * 100:.2f}%")
    else:
        st.success("✅ No Heart Disease Detected")
        st.write(f"Risk Probability: {probability[1] * 100:.2f}%")