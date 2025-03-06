# Introduction  
This project aims to develop a machine learning model to classify participants based on health and lifestyle survey data, optimizing to ensure higher-risk cases are correctly prioritized.

# Problem Statement
The goal of this project is to determine a predictive model that accuractely classifies individuals into different obesity levels. Given the ordinal nature of obesity classification, it is important to not only assign the correct class, but also ensure that higher-risk cases are ranked above lower-risk cases.To accomplish this, the model is optimized using the One-vs-One ROC-AUC metric, which evaluates how well the model distinguishes between each pair of obesity levels. This ensures that the model effectively distinguishes between obesity categories and minimizes ranking errors, in turn prioritizing individuals based on obesity risk.

# Project Objective
- Develop a machine learning model to classify participants into different obesity levels.
- Analyze dataset features to determine the ones with the highest impact to predictions.
- Compare different classification models and tune hyperparameters to improve generalizations.
- Optimize for One-vs-One ROC-AUC to prioritize individuals with higher obesity risk.
- Evaluate the model using multiple metrics (Accuracy, F1-score, ROC-AUC)

# Dataset
Source: [Estimation of Obesity Levels Based On Eating Habits and Physical Condition](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition).  
Size: 2111 observations, 17 features.  
Features: Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, and MTRANS.  
Target Variable: NObeyesdad (Multi-class classification).  

# Methodology
- Data preprocessing: Looking for missing values, visualizing features, and encoding categorical features.
- Feature engineering: Derived new features such as BMI, Meal_Balance_Ratio, and Active_Transport_Indicator.
- Outlier Detection: Used IQR, Z-scores, and percentile-based outlier detection methods.
- Model selection: Compared Logistic Regression and Decision Tree Classifier.
- Feature importance analysis: Choose the features with the highest importance, to reduce complexity in modeling.
- Hyperparameter tuning: Used GridSearchCV and optimized for ROC-AUC.

# Model Performance

### Baseline models:

| Model               | Accuracy |
|---------------------|----------|
| Logistic Regression | 60%      | 
| Decision Tree       | 77%      |

### Tuned model: 

| Decision Tree Score | Value |
|---------------------|-------|
| Accuracy            | 73%   |
| Weighted Precision  | 73%   |
| Weighted Recall     | 73%   |
| ROC-AUC-OVO         | 0.91  |

Performance Insights: The tuned model performs well on the extreme obesity cases, but struggles slightly with mid-level classifications.


# Key Findings

- Extreme obesity classes were predicted at a very high accuracy (~98%), but mid-level obesity categories had much lower precision and recall.
- Feature selection improved the model's ability to generalize well to new data, but slightly reduced accuracy from 77% to 73%.
- ROC-AUC One-vs-One helped improve ranking of obesity levels, to prioritize higher-risk cases.

# Installation

### Prerequisites
Ensure Python is installed, along with the required libraries:  
`pip install pandas numpy scikit-learn matplotlib seaborn`

### Running the project
1. Clone the repository:

2. Run Jupyter notebook or Python script:  
`jupyter notebook`

