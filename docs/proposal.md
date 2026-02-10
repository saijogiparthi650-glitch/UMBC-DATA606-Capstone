# 1. Title and Author

## Project Title  
**Credit Card Default Risk Prediction using ML**

Prepared for UMBC Data Science Master Degree Capstone  
Instructor: Dr. Chaojie Wang  

**Author:** Sai Vara Prasad Jogiparthi  

**GitHub Repository:**  
https://github.com/saijogiparthi650-glitch/UMBC-DATA606-Capstone  

**LinkedIn Profile:**  
https://www.linkedin.com/in/sai-vara-prasad-jogiparthi/

---

# 2. Background

Credit card default is a significant financial risk faced by banks and financial institutions worldwide. When customers fail to make timely payments on their credit card balances, it can lead to financial losses, increased operational costs, and reduced profitability for lenders. Accurately identifying customers who are likely to default is therefore critical for effective credit risk management.

With the increasing availability of large-scale financial datasets, machine learning techniques have become an important tool for predicting credit risk. By analyzing historical customer information such as credit limits, repayment history, billing amounts, and payment behavior, supervised learning models can be trained to estimate the probability of future default.

The objective of this project is to develop supervised machine learning models to predict whether a credit card customer will default on their payment in the following month. Using a publicly available dataset containing anonymized and numeric customer-level financial data, this project aims to compare multiple traditional machine learning classification models and identify the most important factors associated with credit card default.

This project focuses exclusively on supervised learning methods, making it well-suited for interpretable modeling and practical financial decision-making.

---

## Research Questions

1. Can historical credit card customer data be used to accurately predict default risk using supervised machine learning models?
2. Which customer attributes and payment behaviors are most strongly associated with credit card default?
3. How do different supervised classification models compare in terms of predictive performance?
4. What evaluation metrics are most appropriate for assessing default prediction models in a financial risk context?

---

# 3. Data

## Data Source

The dataset used in this project is the **Default of Credit Card Clients Dataset**, originally published by the UCI Machine Learning Repository.  
This dataset contains anonymized financial and demographic information for credit card clients and is widely used for academic research in credit risk modeling.

For this project, a **CSV-formatted mirror version of the dataset available on Kaggle** was used for data access and implementation.  
The Kaggle version is a direct mirror of the original UCI dataset and contains the same observations, features, and target variable without modification.

The dataset was accessed from the following Kaggle link:

https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset
---

## Data Size

- Number of rows: **30,000**
- Number of columns: **23**
- File size: Approximately **5 MB**

This dataset is sufficiently large to support robust supervised machine learning modeling and cross-validation.

---

## Time Period

The dataset contains credit card payment information recorded over a **six-month historical period** for each customer.  
The target variable indicates whether the customer defaulted in the **following month**, making this a forward-looking prediction task.

---

## Unit of Analysis

Each row in the dataset represents an **individual credit card customer**.  
The dataset is fully anonymized and does not contain any personally identifiable information.

---

## Data Dictionary (Key Columns)

| Column Name | Data Type | Description |
|------------|----------|-------------|
| LIMIT_BAL | Numeric | Credit limit assigned to the customer |
| AGE | Numeric | Age of the customer in years |
| SEX | Numeric | Gender of the customer (encoded numerically) |
| EDUCATION | Numeric | Education level (encoded numerically) |
| MARRIAGE | Numeric | Marital status (encoded numerically) |
| PAY_0 to PAY_6 | Numeric | Repayment status for the past six months |
| BILL_AMT1 to BILL_AMT6 | Numeric | Monthly bill amounts for the past six months |
| PAY_AMT1 to PAY_AMT6 | Numeric | Monthly payment amounts for the past six months |
| default.payment.next.month | Binary | Indicates whether the customer defaulted (1) or not (0) |

All features in the dataset are numeric, making it well-suited for traditional supervised machine learning techniques.

---

## Target Variable

The target variable for this project is:

**`default.payment.next.month`**

- `0` indicates that the customer did not default
- `1` indicates that the customer defaulted on their payment in the following month

This binary outcome defines a supervised classification problem.

---

## Feature Variables

The feature variables used for model training include:

- Credit limit and demographic information
- Historical repayment status indicators
- Monthly billing amounts
- Monthly payment amounts

These features capture customer financial behavior and credit usage patterns over time. Feature scaling and preprocessing will be applied as required by specific machine learning models.
