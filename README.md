# 🩺 Disease Prediction ML App

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-RandomForest-orange)
![Platform](https://img.shields.io/badge/Platform-Streamlit%20Cloud-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-success)

```
██████╗ ███████╗███████╗██╗███████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██║██╔════╝██╔════╝██╔══██╗
██████╔╝█████╗  █████╗  ██║███████╗█████╗  ██████╔╝
██╔══██╗██╔══╝  ██╔══╝  ██║╚════██║██╔══╝  ██╔══██╗
██║  ██║███████╗██║     ██║███████║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
       DISEASE PREDICTION ML APP 🩺
```

### 🔗 **Live Demo:**  
👉 https://disease-prediction-ml-b3pdqhkcdrjcylgpfgzdxo.streamlit.app/

---

## 📌 Overview

This project is a complete end-to-end **Machine Learning Disease Prediction System** that predicts the most likely diseases based on user-selected symptoms.

It includes:

- Data preprocessing  
- Multi-label symptom encoding  
- Random Forest model training  
- Model evaluation with classification metrics  
- Interactive Streamlit frontend  
- Deployment on Streamlit Cloud  
- Full project documentation

This project is designed for **learning**, **portfolio building**, and **real-world ML practice**.

---

## 🖼️ Screenshots

### 🔹 **Home Page – App Loaded Successfully**
![App Screenshot 1](images/Screenshot%202025-11-21%20012858.png)

### 🔹 **Prediction Result – Top 3 Disease Predictions**
![App Screenshot 2](images/Screenshot%202025-11-21%20012909.png)

---

## 🚀 Features

- 🧠 Predicts **top 3 most probable diseases**
- 🧩 Uses **MultiLabelBinarizer** to encode symptoms
- 🌲 Random Forest classifier with multi-class capability
- 🌐 Fully interactive **Streamlit web interface**
- 📊 Includes detailed model evaluation
- 🔄 Deployed online for instant demo access

---

## 🗂️ Project Structure

```
disease-prediction-ml/
│
├── notebooks/
│   └── Disease_Prediction.ipynb       # Day 1–4 EDA, preprocessing, training, saving
│
├── src/
│   └── app.py                         # Streamlit Application (Day 5)
│
├── models/
│   └── disease_model.joblib           # Trained RandomForest model
│
├── data/
│   └── README.md                      # Dataset source/description
│
├── results/
│   ├── metrics.txt                    # Evaluation metrics (precision, recall, F1-score)
│   └── confusion_matrix.png           # Confusion matrix visualization
│
└── requirements.txt                   # Dependencies for running the project
```

---

## 🧠 Model Details

- **Algorithm:** RandomForestClassifier  
- **Encoding:** MultiLabelBinarizer  
- **Symptoms:** 40+  
- **Diseases:** 18 classes  
- **Train/Test Split:** 80/20  
- **Evaluation:** Classification Report + Confusion Matrix  

---

## 📊 Results

Detailed metrics available in:

```
results/metrics.txt
```

Includes:

- Precision  
- Recall  
- F1-score  
- Per-class performance  
- Overall accuracy  

---

## ▶️ Run Project Locally

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/Debidutta3/disease-prediction-ml.git
cd disease-prediction-ml
```

### 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app:
```bash
streamlit run src/app.py
```

---

## 🌐 Deployment

The app is deployed using **Streamlit Cloud** for public access.

🔗 **Live Demo:**  
https://disease-prediction-ml-b3pdqhkcdrjcylgpfgzdxo.streamlit.app/

---

## ⚠️ Disclaimer

This app is created for **educational and demonstration purposes only**.  
It is **not intended for real medical diagnosis** or clinical use.

---
