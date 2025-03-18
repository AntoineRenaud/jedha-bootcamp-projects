import mlflow
import os

import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.metrics import root_mean_squared_error

def main():
    #loading dataset
    df = pd.read_csv('src/get_around_pricing_project.csv', index_col=0)

    #cleaning dataset
    #convert numerical features to float to solve warning on mlflow
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].astype(float)
            
    # Group underrepesented categories under 'Other'

    #create a list of all categorical features in the dataset
    cat_feature_list = [col for col in df.columns if not pd.api.types.is_numeric_dtype(df[col])]

    for feature in cat_feature_list:
        feature_count = df[feature].value_counts()
        feature_percent = feature_count / feature_count.sum() * 100
        df[feature] = df[feature].apply(lambda x: x if x in feature_count.index[feature_percent > 1] else 'other')

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

    # Define models and parameter grids
    params = {
        'linear_regression': {
            'model': LinearRegression(),
            'params': {
                # 'alpha': [0.5, 1, 10]
            }
        },

        'ridge': {
            'model': Ridge(),
            'params': {
                'regressor__alpha': [0.5, 1, 10]
            }
        },

        'lasso': {
            'model': Lasso(),
            'params': {
                'regressor__alpha': [0.1, 1, 10]
            },
        },

        'svr': {
            'model': SVR(),
            'params': {
                'regressor__C': [0.1, 1, 10],
                'regressor__degree':[2, 3, 4],
                'regressor__kernel': ['poly']
            }
        }
    }


    EXPERIMENT_NAME="get-around"

    mlflow.set_tracking_uri(os.getenv("MLFLOW_APP_URI"))

    mlflow.set_experiment(EXPERIMENT_NAME)
    input_example = X_train[:5]

    # Run GridSearchCV for each model and log results
    for model_name, mp in params.items():
        model = mp['model']
        params = mp['params']

        regressor_model= Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("regressor", model)
            ]
        )

        # Set up GridSearchCV
        print(f"model is : {model}")

        grid_search = GridSearchCV(regressor_model, params, cv=3, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train)

        y_train_pred = grid_search.best_estimator_.predict(X_train)
        y_test_pred = grid_search.best_estimator_.predict(X_test)   

        r2score = grid_search.best_estimator_.score(X_train, y_train)
        print("R2 score on training set :", r2score)
        rmse = root_mean_squared_error(y_test, y_test_pred)
        print("RMSE score on test set :", rmse)

        # Log parameters and metrics to MLflow
        with mlflow.start_run(run_name=model_name):
            mlflow.log_params(grid_search.best_params_)
            mlflow.log_metric("best_score", grid_search.best_score_)

            # Log the model
            mlflow.sklearn.log_model(grid_search.best_estimator_, "model", input_example=input_example)
            
            # Log Metric 
            mlflow.log_metric('r2_score', r2score)
            mlflow.log_metric('rmse', rmse)

    print("MLflow experiment completed.")



if __name__ == "__main__":
    main()
