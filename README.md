# 🚀 Machine Learning Pipeline

## 📌 Overview

This project demonstrates a complete **Machine Learning pipeline** for predicting house prices using features such as area, number of bedrooms, and bathrooms.

The pipeline follows a structured approach used in real-world ML systems, including data preprocessing, feature engineering, model training, evaluation, and deployment.

The final model is deployed using a **Streamlit web application**, enabling users to input data and get real-time predictions.

---

## 🎯 Objective

The objective of this project is to:

- Build an end-to-end Machine Learning pipeline  
- Preprocess and clean data  
- Perform feature engineering  
- Train multiple ML models  
- Evaluate and compare models  
- Select and save the best model  
- Deploy the model using a web interface  

---

## 🧠 Machine Learning Pipeline


Problem Definition
↓
Data Collection
↓
Data Preprocessing
↓
Exploratory Data Analysis (EDA)
↓
Feature Engineering
↓
Train-Test Split
↓
Model Training
↓
Model Evaluation
↓
Model Comparison
↓
Model Saving
↓
Deployment (Streamlit App)


---

## 📂 Project Structure


ML-House-Price-Prediction/

├── 01_load_dataset.py
├── 02_data_preprocessing.py
├── 03_eda.py
├── 04_feature_engineering.py
├── 05_model_training.py
├── 06_model_evaluation.py
├── 07_model_saving.py
├── app.py

├── data.csv
├── clean_data.csv
├── X_processed.csv
├── y.csv
├── model.pkl

├── requirements.txt
└── README.md


---

## ⚙️ Pipeline Steps

### 1️⃣ Data Loading
- Load dataset using pandas  
- Check dataset structure and missing values  

---

### 2️⃣ Data Preprocessing
- Handle missing values  
- Remove duplicate records  
- Fix data types  

---

### 3️⃣ Exploratory Data Analysis (EDA)
- Analyze data distribution  
- Identify relationships between features  
- Generate insights  

---

### 4️⃣ Feature Engineering
- Encode categorical variables  
- Scale numerical features  
- Prepare data for modeling  

---

### 5️⃣ Train-Test Split
- Split dataset into training and testing sets  
- Ensure proper model validation  

---

### 6️⃣ Model Training
Models used:
- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

---

### 7️⃣ Model Evaluation
Metrics used:
- R² Score  
- Root Mean Squared Error (RMSE)  

---

### 8️⃣ Model Comparison
- Compare performance of multiple models  
- Select best-performing model  

---

### 9️⃣ Model Saving
- Save final model using joblib  
- Output file: `model.pkl`  

---

### 🔟 Deployment
- Build Streamlit web application  
- Take user input  
- Predict house price  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  
- Joblib  

---

## 💻 Installation

Install required libraries:


pip install -r requirements.txt


---

## ▶️ Running the Pipeline

Run scripts in order:


python 01_load_dataset.py
python 02_data_preprocessing.py
python 03_eda.py
python 04_feature_engineering.py
python 05_model_training.py
python 06_model_evaluation.py
python 07_model_saving.py


---

## ▶️ Run Application


streamlit run app.py


Open in browser:


http://localhost:8501


---

## 📊 Dataset

The project uses a **House Price dataset** with features:

- Area  
- Bedrooms  
- Bathrooms  
- Price (target variable)  

---

## 🌍 Applications

- Real estate price prediction  
- Property valuation systems  
- Investment analysis tools  

---

## 🎓 Learning Outcomes

- End-to-end ML pipeline development  
- Data preprocessing and feature engineering  
- Model training and evaluation  
- Model comparison techniques  
- Deployment using Streamlit  

---

## 👨‍💻 Author

Harsh Chauhan  
AI & Data Science Enthusiast
💎 This is now PERFECT

✔ Machine Learning (not Data Science)
✔ Clean structure
✔ Proper pipeline steps
✔ GitHub-ready
✔ Interview-ready

🚀 Next Step

Now your portfolio has:

✔ Data Science Pipeline
✔ Machine Learning Pipeline
✔ NLP + RAG

👉 Next best move:

Customer Churn Prediction (Classification ML Project)

If you want:

👉 I’ll build full churn project like this 😎🔥
