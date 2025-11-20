import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Disease Predictor", page_icon="🩺", layout="centered")

st.write("App loaded successfully.")

# Load model + encoder
data = joblib.load("models/disease_model.joblib")
model = data['model']
mlb = data['mlb']

st.write("Symptoms found in model:", mlb.classes_)

# Title
st.title("Disease Prediction App")

st.write("Select symptoms below:")

# Symptom selection
symptoms = st.multiselect("Select Symptoms:", mlb.classes_)

# Predict button
if st.button("Predict"):
    if len(symptoms) == 0:
        st.warning("Please select at least one symptom.")
    else:
        input_vec = mlb.transform([symptoms])
        probs = model.predict_proba(input_vec)[0]

        top_idx = np.argsort(probs)[::-1][:3]

        st.subheader("Top predicted diseases:")
        for i in top_idx:
            st.write(f"**{model.classes_[i]}** — {probs[i] * 100:.2f}%")

        st.info("Not for medical use.")

