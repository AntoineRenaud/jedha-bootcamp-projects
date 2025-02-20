docker build . -t audio-classification-api
docker run -it -v "${PWD}:/home/app" -p 4000:4000 -e PORT=4000 audio-classification-api