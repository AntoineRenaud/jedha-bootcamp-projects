docker build . -t netflix-api
docker run -it -v "${PWD}:/home/app" -p 4000:4000 -e PORT=4000 netflix-api