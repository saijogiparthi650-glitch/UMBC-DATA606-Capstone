# Credit Card Default Prediction using Machine Learning

DATA 606 Capstone Project  
University of Maryland, Baltimore County (UMBC)

Prepared for: Dr. Chaojie Wang  
Author: Sai Vara Prasad Jogiparthi

---

## Project Overview

This project focuses on predicting credit card default risk using machine learning techniques. Multiple machine learning models were trained and evaluated using the UCI Credit Card Default dataset. The final model was deployed using Streamlit to provide real-time default risk prediction.

---

## Repository Structure

- `app/` → Streamlit web application files  
- `data/` → Dataset files  
- `docs/` → Project report, presentation, and supporting documents  
- `notebooks/` → Jupyter notebooks for EDA and model building  
- `xgboost_model.pkl` → Trained machine learning model  

---

## Project Links

### Live Streamlit Application
https://credit-default-predict.streamlit.app/

### YouTube Presentation
https://youtu.be/zoaPDaGhoqY

### GitHub Repository
https://github.com/saijogiparthi650-glitch/UMBC-DATA606-Capstone

### LinkedIn Profile
https://www.linkedin.com/in/sai-vara-prasad-jogiparthi/

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Jupyter Notebook

---

## Machine Learning Models Used

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- XGBoost Classifier

---

## Final Model

XGBoost Classifier achieved the best overall performance for predicting customer default risk.

Performance:
- Accuracy: ~75%
- Strong performance on non-default cases
- Moderate performance on default cases

---

## Streamlit Application Features

The application allows users to:

- Enter customer financial details
- Predict default probability
- View customer risk level instantly
- Receive real-time prediction results

---

## Dataset

Dataset used:
UCI Credit Card Default Dataset

- Approximately 30,000 customer records
- Includes demographic, billing, and payment history information
- Target variable predicts default payment in the next month

---

## Conclusion

This project demonstrates how machine learning can be applied to solve real-world financial risk prediction problems. The final solution includes data analysis, model development, evaluation, and deployment through a Streamlit web application.
