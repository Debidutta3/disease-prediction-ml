# 🩺 Disease Prediction App  
Predict diseases based on symptoms using a trained Machine Learning model.

### 🔗 **Live Demo:**  
https://disease-prediction-ml-b3pdqhkcdrjcylgpfgzdxo.streamlit.app/

---

## 📌 Overview

This is an end-to-end Machine Learning project that predicts the most likely disease based on selected symptoms.  
The project includes:

- Data preprocessing  
- MultiLabel symptom encoding  
- Random Forest model training  
- Model evaluation (precision, recall, F1-score)  
- Interactive **Streamlit web app**  
- Deployment on **Streamlit Cloud**

> ⚠️ For educational and demonstration purposes only. Not for real medical diagnosis.

---

## 🖼️ App Screenshots

### **🔹 Homepage – App Loaded Successfully**
![App Screenshot 1](images/Screenshot%202025-11-21%20012858.png)

### **🔹 Prediction Example**
![App Screenshot 2](images/Screenshot%202025-11-21%20012909.png)

---

## 🚀 Features

- 🧠 Predict top 3 likely diseases  
- 🧩 MultiLabelBinarizer symptom encoding  
- 🌲 Random Forest classifier  
- 🌐 Live web app with Streamlit  
- 📊 Classification report included  
- 🦾 Fully reproducible Colab notebook  

---

## 🗂️ Project Structure

```
disease-prediction-ml/
│
├── notebooks/
│   └── Disease_Prediction.ipynb       # Day 1–4 end-to-end work
│
├── src/
│   └── app.py                         # Streamlit application
│
├── models/
│   └── disease_model.joblib           # Trained model
│
├── data/
│   └── README.md                      # Dataset description
│
├── results/
│   ├── metrics.txt                    # Evaluation metrics
│   └── confusion_matrix.png           # (optional)
│
└── requirements.txt                   # Dependencies
```

---

## 🧠 Model Details

- **Algorithm:** RandomForestClassifier  
- **Encoding:** MultiLabelBinarizer  
- **Classes:** 18 diseases  
- **Symptoms:** 40+  
- **Train/Test Split:** 80/20  

---

## 📊 Metrics

Metrics file:  
`results/metrics.txt`

---

## ▶️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Debidutta3/disease-prediction-ml.git
cd disease-prediction-ml
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit app
```bash
streamlit run src/app.py
```

---

## 🌐 Deployment

The app is deployed on **Streamlit Cloud**:  
🔗 https://disease-prediction-ml-b3pdqhkcdrjcylgpfgzdxo.streamlit.app/

