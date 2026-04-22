# 1. Title and Author

## Project Title  
**Credit Card Default Risk Prediction using Machine Learning**

Prepared for UMBC Data Science Master Degree Capstone  
Instructor: Dr. Chaojie Wang  

**Author:** Sai Vara Prasad Jogiparthi  

**GitHub Repository:**  
https://github.com/saijogiparthi650-glitch/UMBC-DATA606-Capstone  

**LinkedIn Profile:**  
https://www.linkedin.com/in/sai-vara-prasad-jogiparthi/

**PowerPoint Presentation:**  
https://docs.google.com/presentation/d/e/2PACX-1vRdqy-dE-sWMFEmpXQ0W5YVn2Lq4ZvsRmJz3T4arNuClxyoo_hxff5P762zV9vP-BTSvbr22oHic82j/pub?start=false&loop=false&delayms=3000

**YouTube Video:**  


---

# 2. Background

Credit card default is a major financial risk for banks and financial institutions. When customers fail to make payments, it leads to financial losses and increased risk exposure. Traditional risk assessment methods are often manual and inefficient.

With the availability of large financial datasets, machine learning can be used to automate and improve default prediction. By analyzing customer demographics, payment history, and financial behavior, predictive models can identify high-risk customers.

## Research Questions

1. Can customer financial data be used to predict credit card default?  
2. Which features are most important in predicting default risk?  
3. Which machine learning model performs best for this problem?  
4. How can model predictions be used in a practical application?  

---

# 3. Data

## Data Source

- UCI Machine Learning Repository  
- Kaggle mirror dataset:  
  https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset  

## Data Size and Shape

- Rows: ~30,000  
- Columns: 23  
- Size: ~5 MB  

## Time Period

- 6 months of historical financial data  
- Target predicts default in the following month  

## Unit of Analysis

Each row represents a **credit card customer**.

## Data Dictionary (Key Features)

| Column | Description |
|--------|------------|
| LIMIT_BAL | Credit limit |
| AGE | Customer age |
| SEX | Gender |
| EDUCATION | Education level |
| MARRIAGE | Marital status |
| PAY_0 – PAY_6 | Repayment history |
| BILL_AMT1 – BILL_AMT6 | Monthly bill amounts |
| PAY_AMT1 – PAY_AMT6 | Payment amounts |
| default.payment.next.month | Target variable |

## Target Variable

- **default.payment.next.month**
  - 0 = No default  
  - 1 = Default  

## Features

- Demographics  
- Credit limit  
- Payment history  
- Billing amounts  
- Payment amounts  

---

# 4. Exploratory Data Analysis (EDA)

EDA was performed using Python (Pandas, Plotly Express).

## Key Findings

- Dataset is moderately imbalanced (~22% defaults)  
- No missing values found  
- 35 duplicate rows removed  
- Payment history strongly correlates with default risk  
- Customers with delayed payments are more likely to default  
- Lower payment amounts increase default probability  

## Data Structure

- Clean and tidy dataset  
- Each row = one customer  
- No additional restructuring required  

---

# 5. Model Training

## Models Used

- Logistic Regression  
- Decision Tree  
- K-Nearest Neighbors (KNN)  
- Random Forest  
- XGBoost  

## Training Approach

- Train-test split (80/20)  
- Implemented using **scikit-learn** and **XGBoost**  
- Developed using Jupyter Notebook  

## Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  

## Best Model

**XGBoost Classifier** performed the best.

### Performance:
- Accuracy: ~75%  
- Strong performance on non-default cases  
- Moderate performance on default cases  

---

# 6. Application of the Trained Models

A web application was developed using **Streamlit**.

## Features

- User inputs customer financial details  
- Model predicts default risk  
- Displays:
  - Risk level (High / Low)  
  - Probability score  

## Purpose

This tool can assist banks and analysts in making quick credit risk decisions.

---

# 7. Conclusion

This project demonstrates that machine learning can effectively predict credit card default risk using customer financial data.

## Key Outcomes

- Built and compared multiple ML models  
- Identified XGBoost as the best-performing model  
- Found payment history to be the most important factor  
- Developed a working Streamlit application  

## Limitations

- Class imbalance affects recall  
- Model struggles with minority class prediction  

## Future Work

- Apply SMOTE or class balancing techniques  
- Improve model tuning  
- Deploy application to cloud  
- Add explainability (SHAP)  

---

# 8. References

- UCI Machine Learning Repository  
- Kaggle Dataset (Default of Credit Card Clients)  
- Scikit-learn Documentation  
- XGBoost Documentation  
- Streamlit Documentation  
