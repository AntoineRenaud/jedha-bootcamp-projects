# Walmart Sales Prediction Project 🛒📈
This is a fun and practical data science project where I built machine learning models to predict weekly sales at Walmart stores based on various economic indicators like fuel price, unemployment rate, CPI, etc. Let me walk you through what this project entails.

## Project Overview

The goal here was to build a model that can accurately predict weekly sales for Walmart stores. This would help in understanding how external factors influence sales and could be used for future marketing planning. The project is divided into three main parts: 

1. Exploratory Data Analysis (EDA) & Preprocessing: Understanding the data, cleaning it up, and getting it ready for machine learning.
2. Linear Regression Model (Baseline): Building a basic linear regression model to serve as our baseline.
3. Regularized Regression Model: Improving upon the baseline by using regularization techniques (Ridge/Lasso) to avoid overfitting.
     
## Goals

- **Perform EDA** and visualize key insights from the data.
- **Preprocess** the dataset for machine learning (handling missing values, encoding categorical variables, etc.).
- Build a **linear regression model** and evaluate its performance.
- Implement **regularization** techniques to improve model generalization.
- **Fine-tune hyperparameters** using GridSearchCV.
      
## Dataset Description

The dataset used in this project contains information about weekly sales at Walmart stores along with various economic indicators. The features include: 

- **Date:** The week for which the sales are recorded.
- **Sales:** The total sales for that week.
- **Unemployment Rate:** The unemployment rate during that week.
- **Fuel Price:** Average fuel price during that week.
- **CPI (Consumer Price Index):** A measure of inflation.
- Other relevant economic and seasonal factors.

## Approach 
### Exploratory Data Analysis & Preprocessing 

- Analyzed the distribution of sales and other features.
- Handled missing values and outliers.
- Converted categorical variables into numerical format using encoding techniques.
- Split the data into training and testing sets for model evaluation.   

### Linear Regression Model 

- Built a simple linear regression model using scikit-learn.
- Evaluated the model's performance on both training and test datasets.
- Analyzed feature coefficients to understand which factors have the most significant impact on sales.
     

### Regularized Regression 

- Implemented Ridge and Lasso regression to regularize the model and prevent overfitting.
- Used GridSearchCV to find the optimal regularization strength for both models.

## Results

- The baseline linear regression model achieved an R² score of [insert your score] on the test set.
- After applying regularization, the Ridge/Lasso model improved performance with an R² score of [insert your score].
- Insights into key factors influencing sales (e.g., fuel price has a significant negative impact).

## How to Run This Project

1. Install the required dependencies:

```python
pip install -r requirements.txt
```
2. Run the jupyter notebook
