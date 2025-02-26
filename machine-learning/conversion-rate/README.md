# Conversion Rate Challenge Project 

## Project Overview 📄 

The goal of this project is to predict whether users visiting a data science weekly newsletter website will subscribe to the newsletter. By analyzing user behavior and website interaction, we aim to build a model that can predict conversions accurately. This model will help the team understand key factors influencing user decisions and provide actionable insights to improve the conversion rate. 

## Goals 🎯

The project is divided into four main parts: 

***Exploratory Data Analysis (EDA):*** Conduct EDA on the training dataset to understand patterns, distributions, and relationships between variables.  
***Baseline Model:*** Train a baseline model using logistic regression to establish a performance benchmark.  
***Model Improvement:*** Enhance the F1-score by experimenting with feature engineering, hyperparameter tuning, and advanced models like Random Forest or Gradient Boosting.  
***Recommendations:*** Analyze the best-performing model to identify key features influencing conversions and provide strategic recommendations.
     

## Dataset Description 📝

The dataset is split into two files: 

```data_train.csv```: Contains labeled data with both features (X) and the target variable (Y), which indicates whether a user subscribed.  
```data_test.csv```: Unlabeled data where the target variable has been removed, used for making final predictions.
     

## Approach 🛠️
     
### Exploratory Data Analysis (EDA):  
- Analyze distributions of features.
- Check for correlations between variables.
- Identify potential class imbalances in the target variable.
    
### Preprocessing:  
- Handle missing values.
- Encode categorical variables using techniques like one-hot encoding or label encoding.
- Scale numerical features if necessary (e.g., standardization).

### Baseline Model:  
- Implement a logistic regression model as the baseline.
- Evaluate performance using F1-score to handle potential class imbalances.    

### Model Improvement:  
- Experiment with feature engineering (e.g., creating interaction terms, polynomial features).
- Try different algorithms (e.g., Random Forest, Gradient Boosting) and assess their performance.
- Perform hyperparameter tuning using grid search or random search.   

### Final Predictions:  
- Use the best-performing model to make predictions on data_test.csv.
- Submit these predictions for evaluation.
   
### Analysis and Recommendations: 
- Interpret the model's coefficients or feature importances.
- Provide actionable insights based on significant predictors of conversions.
         
     
## Results 📊

The project aims to achieve a high F1-score on both training and test sets, indicating good predictive performance. Additionally, the analysis will yield recommendations for improving the conversion rate by targeting key user segments or enhancing specific website features. 

## Technologies Used 💻

Python Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn
Environment: Jupyter Notebook


## How to Run This Project 🚀 

Run the notebook: Execute the notebook starting with EDA.
     