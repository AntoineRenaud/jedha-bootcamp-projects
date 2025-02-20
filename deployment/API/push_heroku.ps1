heroku container:push web -a get-around-api
heroku container:release web -a get-around-api
heroku logs --tail -a get-around-api