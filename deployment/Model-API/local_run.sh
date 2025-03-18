docker run -it \
    --name get-around-api \
    --env-file .env \
    --rm \
    -p 5000:5000 \
    get-around-api