docker run -it \
  --name mlflow_server \
  --env-file .env \
  --rm \
  -p 4000:4000 \
  -v $(pwd):/home/app \
  sample-mlflow-server