# Projects

## Conversion Rate Challenge

This project involves participating in a machine learning competition, inspired by platforms like Kaggle. The goal is to build a model that predicts whether a user visiting a website will subscribe to the newsletter. The project consists of training a model, improving its performance, and submitting predictions for independent evaluation.

### Objective

To predict newsletter conversions based on user data, improving the newsletter's conversion rate by identifying key features that influence user behavior.
Project Steps

Exploratory Data Analysis (EDA) and Baseline Model
    Analyze the dataset (data_train.csv) and train a baseline model.

Model Improvement
    Optimize the model using feature engineering, feature selection, regularization, and hyperparameter tuning.
    Focus on improving the F1-score for model evaluation.

Prediction Submission
    Generate predictions using the test dataset (data_test.csv) and submit the results.
    Multiple submissions are encouraged for performance testing.

Model Analysis and Recommendations
    Analyze the model's parameters and provide actionable insights to enhance the conversion rate.

### Deliverables

Create visualizations for EDA.
Train at least one model and evaluate its performance (using F1-score, confusion matrices).
Submit predictions to the leaderboard.
Provide analysis and recommendations based on model outcomes.

### Evaluation Metric

F1-Score: The competition's ranking is based on this metric to ensure a balance between precision and recall.

### Getting Started

A project template (02-Conversion_rate_challenge_template.ipynb) is provided, containing a simple logistic regression model. You can modify and extend this template to improve the model and optimize performance.

## Walmart Sales 

### Project Overview

In this project, you’ll build a machine learning model to estimate Walmart's weekly sales with high accuracy. The model will help understand how economic factors influence sales and assist in planning marketing campaigns.

### Dataset

The dataset contains weekly sales data for Walmart stores, along with variables like unemployment rates and fuel prices. Ensure you use the custom dataset provided on JULIE.

### Objectives

Part 1: Perform Exploratory Data Analysis (EDA) and preprocess the data for modeling.
Part 2: Train a linear regression model as a baseline.
Part 3: Mitigate overfitting by training a regularized regression model (Lasso or Ridge).

### Deliverables

Visualizations from the EDA
A linear regression model predicting weekly sales
Performance assessment using a regression metric (e.g., RMSE, MAE)
Interpretation of model coefficients to identify important features
A regularized regression model to reduce overfitting

### Helpers
Part 1: EDA & Preprocessing

Drop rows with missing target values (Weekly_Sales).
Create new features from the Date column (year, month, day, day of week).
Handle outliers using the [X̄−3σ, X̄+3σ] rule for numeric features.
Identify categorical (Store, Holiday_Flag) and numerical variables (Temperature, Fuel_Price, CPI, Unemployment).

Part 2: Baseline Model

Train a linear regression model and assess performance.
Use the .coef_ attribute in scikit-learn’s LinearRegression class to analyze feature importance.

Part 3: Regularized Regression

Train a Ridge or Lasso model to prevent overfitting.
Fine-tune the regularization strength using GridSearchCV.

## Uber pickups

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Uber_logo_2018.svg/1024px-Uber_logo_2018.svg.png)

### Project Overview

This project focuses on identifying "hot-zones" in New York City where Uber drivers should position themselves to reduce passenger wait times. By analyzing Uber pickup data, we aim to create algorithms that recommend optimal locations for drivers at any given time of day.

### Dataset

We will use Uber trip data specific to New York City. The dataset can be found here:

[Uber Trip Data](https://full-stack-bigdata-datasets.s3.eu-west-3.amazonaws.com/Machine+Learning+non+Supervis%C3%A9/Projects/uber-trip-data.zip)

### Objectives

Algorithm Development: Create algorithms to find hot-zones using clustering techniques.
Visualization: Display the results on a map using Python libraries like Plotly.
Temporal Analysis: Describe hot-zones per day of the week.
Algorithm Comparison: Compare results using at least two unsupervised algorithms (e.g., KMeans and DBSCAN).

### Deliverables

A map showcasing hot-zones using any Python library.
Analysis of hot-zones for each day of the week.
A comparison report between at least two clustering algorithms.

### Helpers

Clustering is Your Friend: Use clustering techniques to group pickup locations and identify hot-zones.
Mapping Tools: Utilize Plotly or similar libraries to create interactive maps.
Start Small, Grow Big: Begin with data from a specific day and hour, then generalize your approach to include more time periods.