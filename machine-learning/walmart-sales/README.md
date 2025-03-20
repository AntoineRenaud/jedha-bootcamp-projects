# Walmart Sales Prediction Project 🛒

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Walmart_logo_%282025%3B_Alt%29.svg/800px-Walmart_logo_%282025%3B_Alt%29.svg.png)


This is an in-depth and practical project where machine learning models were developed to forecast weekly sales at Walmart stores based on various economic indicators such as fuel prices, unemployment rates, and Consumer Price Index (CPI).

## Project Overview

The goal here was to build a model that can accurately predict weekly sales for Walmart stores. This would help in understanding how external factors influence sales and could be used for future marketing planning. The project is divided into three main parts: 

1. **Exploratory Data Analysis (EDA) & Preprocessing:** Understanding the data, cleaning it up, and getting it ready for machine learning.
2. **Basic Linear Regression Model :** Building a basic linear regression model to serve as our baseline.
3. **Regularization:** Improving upon the baseline by using regularization techniques (Ridge/Lasso) to avoid overfitting.
    
        
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

## How to Run This Project

1. Install the required dependencies:

```python
pip install -r requirements.txt
```
2. Run the jupyter notebook
