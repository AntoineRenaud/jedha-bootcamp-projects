# MLflow Server Deployment

This folder contains the necessary files and instructions to deploy an MLflow server. MLflow is an open-source platform for managing the end-to-end machine learning lifecycle. The goal is to set up a server that can track experiments, package code into reproducible runs, and share and deploy models.

## Setup
To set up the MLflow server locally, follow these steps:
1. Build the docker image:
```sh
docker build . -t mlflow-server
```

2. Run the server:
```sh
docker run -it --name mlflow_server --env-file .env --rm -p 4000:4000 -v $(pwd):/home/app mlflow-server
```

This will start the MLflow server locally.

Once the server is running, you can access the MLflow UI by navigating to `http://localhost:4000` in your web browser. From there, you can create new experiments, track runs, and manage models.