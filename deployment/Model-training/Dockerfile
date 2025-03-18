FROM python:3.10-slim

WORKDIR /home/app

RUN apt-get update && apt-get install -y git

COPY requirements.txt /dependencies/requirements.txt
RUN pip install -r /dependencies/requirements.txt

COPY . /home/app/

CMD ["python", "train.py"]