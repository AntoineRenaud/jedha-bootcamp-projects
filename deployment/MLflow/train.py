import mlflow
import os
import joblib 

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error

from mlflow.models import infer_signature


EXPERIMENT_NAME="get-around"

mlflow.set_tracking_uri(os.environ["APP_URI"])
mlflow.set_experiment(EXPERIMENT_NAME)
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
# mlflow.sklearn.autolog()


#loading data

df = pd.read_csv('src/get_around_pricing_project.csv', index_col=0)

#cleaning dataset
#convert numerical features to float to solve warning on mlflow
for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].astype(float)
        
#group underrepesented categories under 'Other'
car_model_counts = df['model_key'].value_counts()
car_model_selected = car_model_counts[car_model_counts.values > 50]
df['model_key']=df['model_key'].apply(lambda x: x if x in car_model_selected.index else 'Other')

#split into train and test set
X = df.drop(['rental_price_per_day'], axis=1)
y = df['rental_price_per_day']

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Definning categorical and numeric features :
numeric_features = []
categorical_features = []


for column in X.columns:
    if pd.api.types.is_numeric_dtype(X[column]) and not pd.api.types.is_bool_dtype(X[column]):
        numeric_features.append(column)
    else:
        categorical_features.append(column)


#create preprocessing pipeline
numeric_transformer = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
    ]
)

categorical_transformer = Pipeline(
    steps=[
        # some category might be present in set and not in another. the OneHotEncoder will simply ignore such category.
        ("encoder",OneHotEncoder(drop='first'))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)



with mlflow.start_run(experiment_id = experiment.experiment_id, run_name='preprocessor'):

    # Save the preprocessor locally
    joblib.dump(preprocessor, 'preprocessor.pkl')
    
    # Log the preprocessor as an artifact in MLflow
    mlflow.log_artifact('preprocessor.pkl', artifact_path='preprocessor')
    
models = [
    LinearRegression(),
    Ridge(alpha=0.5),
    Lasso(alpha=0.1)
]
    
for model in models:
    
    with mlflow.start_run(experiment_id = experiment.experiment_id, run_name=model.__class__.__name__):
    
        model.fit(X_train,y_train)
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        
        signature = infer_signature(X_train, model.predict(X_train))
        
        model_info = mlflow.sklearn.log_model(
            sk_model=model, artifact_path="model", signature=signature
        )
        
        
        print(f"model is : {model}")
        
        r2score = model.score(X_train, y_train)
        print("R2 score on training set :", r2score)
        mse=mean_squared_error(y_train, y_train_pred)
        print("MSE score on training set :", mse)
        rmse=root_mean_squared_error(y_train, y_train_pred)
        print("RMSE score on training set :", rmse)
        
        # Log Metric 
        mlflow.log_metric('r2_score', r2score)
        mlflow.log_metric('mse',mse)
        mlflow.log_metric('rmse', rmse)

        # Log model 
        mlflow.sklearn.log_model(model, model.__class__.__name__)
