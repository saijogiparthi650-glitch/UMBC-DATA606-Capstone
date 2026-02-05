# 1. Title and Author

## Project Title  
**Predicting Emergency Department Wait Times Using CMS Hospital Performance Data**

Prepared for UMBC Data Science Master Degree Capstone  
Instructor: Dr. Chaojie Wang  

**Author:** Sai Vara Prasad Jogiparthi  

**GitHub Repository:**  
https://github.com/saijogiparthi650-glitch/UMBC-DATA606-Capstone

**LinkedIn Profile:**  
https://www.linkedin.com/in/sai-vara-prasad-jogiparthi/


---

# 2. Background

Emergency Departments (EDs) are an essential part of the healthcare system, as they provide immediate care to patients with urgent and critical medical needs. However, long wait times in emergency departments are a common problem and can negatively affect patient satisfaction, quality of care, and overall hospital efficiency.

Emergency department wait times can be influenced by many factors such as hospital location, patient volume, reporting period, and operational efficiency. Understanding these factors is important for hospitals and healthcare policymakers who want to improve patient flow and reduce delays.

The goal of this project is to analyze emergency department wait time data published by the Centers for Medicare & Medicaid Services (CMS) and use supervised regression techniques to predict average emergency department wait times. By building regression models using publicly available hospital-level data, this project aims to identify patterns and key factors associated with longer wait times.

## Research Questions

1. Can hospital-level CMS data be used to predict emergency department wait times?
2. How do emergency department wait times vary across hospitals and regions?
3. Which factors are most strongly associated with longer emergency department wait times?
4. How well do different regression models perform in predicting ED wait times?

---

# 3. Data

## Data Source

The dataset used in this project is the **CMS Hospital Timely and Effective Care – Hospital** dataset.  
This dataset is publicly available and published by the Centers for Medicare & Medicaid Services (CMS).

Due to GitHub file size limitations, the raw dataset is not included in this repository.  
The dataset can be accessed and downloaded from the following link:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

---

## Data Size

- Approximate file size: **34 MB**
- Number of rows: **138,182**
- Number of columns: **16**

---

## Time Period

The dataset contains hospital performance measures reported over recent years.  
Each record is associated with a specific reporting period defined by a start date and end date.

---

## Unit of Analysis

Each row in the dataset represents a **hospital-level performance measure** for a specific hospital and reporting period.  
The data is aggregated at the hospital level and does not include any patient-level or personally identifiable information.

---

## Data Dictionary (Key Columns)

| Column Name | Data Type | Description | Possible Values |
|------------|----------|-------------|----------------|
| Facility ID | Categorical | Unique identifier for each hospital | Alphanumeric |
| Facility Name | Categorical | Name of the hospital | Text |
| City/Town | Categorical | City where the hospital is located | Text |
| State | Categorical | U.S. state of the hospital | State abbreviations |
| ZIP Code | Numeric | ZIP code of the hospital | Integers |
| County/Parish | Categorical | County or parish name | Text |
| Condition | Categorical | Type of healthcare condition | Emergency Department, others |
| Measure ID | Categorical | CMS identifier for the measure | Alphanumeric |
| Measure Name | Categorical | Description of the performance measure | Text |
| Score | Numeric / Categorical | Reported performance value | Minutes, text values |
| Sample | Numeric / Categorical | Sample size used for the measure | Numeric or “Not Available” |
| Start Date | Date | Beginning of reporting period | Date |
| End Date | Date | End of reporting period | Date |

---

## Target Variable

The target variable for this project will be the **average emergency department wait time**, measured in minutes.  
This value will be obtained from the `Score` column after filtering the dataset to include only emergency department wait time measures.

---

## Feature Variables

Potential feature variables for the regression models include:

- Hospital location (state, county, ZIP code)
- Reporting time period (derived from start and end dates)
- Emergency department volume indicators
- Sample size of reported measures

These variables will be processed and encoded as needed before building regression models.
