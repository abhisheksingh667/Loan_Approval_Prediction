# 🏦 Loan Approval Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow)

An end-to-end Machine Learning project that predicts whether a loan application will be **Approved** or **Rejected** based on applicant information such as CIBIL score, income, assets, loan amount, and loan term.

The project covers the complete Machine Learning workflow including data preprocessing, feature engineering, model training, evaluation, deployment, and an interactive Streamlit web application.

---

# 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Manual evaluation is time-consuming and prone to inconsistencies.

This project automates the loan approval process by training multiple Machine Learning models to predict loan approval based on applicant details.

---

# 🎯 Objectives

- Perform Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Comparison
- Cross Validation
- Model Deployment using Streamlit

---

# 📂 Dataset Information

The dataset contains information about loan applicants including:

- Number of Dependents
- Education
- Self Employed Status
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets
- Commercial Assets
- Luxury Assets
- Bank Assets

Target Variable

- Loan Status
    - Approved
    - Rejected

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

# ⚙️ Machine Learning Workflow

### 1. Data Cleaning

- Removed unnecessary columns
- Checked missing values
- Removed duplicates
- Encoded categorical variables

---

### 2. Feature Engineering

Created new features:

- Total Assets
- Loan Income Ratio
- Asset Coverage Ratio

---

### 3. Feature Scaling

- StandardScaler

---

### 4. Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

---

# 📊 Model Performance

| Model | Accuracy |
|---------|---------|
| Logistic Regression | **89.43%** |
| Decision Tree | **100%** |
| Random Forest | **100%** |
| XGBoost | **99.93%** |

---

# 📈 Feature Importance

Top important features learned by Random Forest:

| Feature | Importance |
|---------|-----------|
| CIBIL Score | 78.67% |
| Loan Term | 6.08% |
| Loan Income Ratio | 3.68% |
| Asset Coverage Ratio | 2.48% |

The model identified **CIBIL Score** as the most influential feature in predicting loan approval.

---

# 💻 Streamlit Web Application

The project includes an interactive web application where users can:

- Enter applicant details
- Predict loan approval
- View prediction instantly
- Simple and responsive interface

---

# 📁 Project Structure

```
Loan_Approval_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── loan_approval_dataset.csv
│
├── models/
│   ├── loan_approval_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── Loan_Approval_Prediction.ipynb
│
└── screenshots/
```

---

# 🔮 Future Improvements

- Hyperparameter Optimization
- SHAP Explainability
- Docker Deployment
- Cloud Deployment (AWS/Azure)
- REST API using FastAPI
- User Authentication
- Database Integration

---

# 🎓 Key Learnings

Through this project I gained hands-on experience in:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Classification Algorithms
- Feature Importance Analysis
- Cross Validation
- Model Serialization
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

# 👨‍💻 Author

**Abhishek Singh**

Machine Learning | Data Science | AI Enthusiast

LinkedIn:
www.linkedin.com/in/abhishek-singh-8bb62221b

GitHub:
https://github.com/abhisheksingh667

---

## ⭐ If you found this project useful, don't forget to Star this repository!
