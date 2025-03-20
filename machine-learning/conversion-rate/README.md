# Conversion Rate Challenge Project 📈

This project aims to **predict** whether users **will subscribe** to the weekly newsletter of **www.datascienceweekly.org** using supervised machine learning techniques.

## Project Overview

The project is divided into four main parts: 

***Exploratory Data Analysis (EDA):*** Conduct EDA on the training dataset to understand patterns, distributions, and relationships between variables.  
***Baseline Model:*** Train a baseline model using logistic regression to establish a performance benchmark.  
***Model Improvement:*** Enhance the F1-score by experimenting with feature engineering, hyperparameter tuning, and advanced models like Random Forest or Gradient Boosting.  
***Recommendations:*** Analyze the best-performing model to identify key features influencing conversions and provide strategic recommendations.
     

## Dataset Description

The dataset is split into two files: 

```conversion_data_train.csv```: Contains labeled data with both features (X) and the target variable (Y), which indicates whether a user subscribed.  
```conversion_data_test.csv```: Unlabeled data where the target variable has been removed, used for making final predictions.  
```conversion_data_test_predictions.csv```: Contains predictions from the best algorithm.  
```conversion_data_test_labels.csv```: Contains true values to compare predictions with.

## Approach
     
- **Exploratory Data Analysis (EDA):** Analyze feature distributions, correlations, and class imbalances in the target variable.
- **Preprocessing:** Handle missing values, encode categorical variables, and scale numerical features as needed.
- **Baseline Model:** Implement logistic regression to establish a performance benchmark using F1-score.
- **Model Improvement:** Experiment with advanced algorithms (e.g., Random Forest, Gradient Boosting) and hyperparameter tuning via grid or random search.
- **Final Predictions:** Generate predictions on the test dataset and submit for evaluation.
- **Analysis & Recommendations:** Interpret model outputs to provide actionable insights aimed at enhancing user engagement and conversion rates.


## How to Run This Project

1. Install the required dependencies:

```python
pip install -r requirements.txt
```
2. Run the jupyter notebook 