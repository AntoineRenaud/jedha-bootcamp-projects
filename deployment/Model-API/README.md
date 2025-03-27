# Model-API

This FastAPI server provides an endpoint that allows users to request a prediction from the model. The model will be loaded from the MLflow server. You can use the `/predict` endpoint to send data and receive predictions.

For example, you can make a POST request to `http://localhost:5000/predict` with the necessary input data, and the server will return the prediction based on the model loaded from the MLflow server.

## Setup

To set up and run the FastAPI server locally, follow these steps:

1. Build the docker image:
```bash
docker build . -t get-around-api
```
2. Set your credentials in the .env file:
```sh
MLFLOW_APP_URI=mlflow_server_adress
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_key_id
```
2. Run the FastAPI server locally using this command:
```bash
docker run -it --name get-around-api --env-file .env --rm -p 5000:5000 get-around-api
```

## Usage

Once the server is running, you can access the API documentation at `http://localhost:5000/docs`.

