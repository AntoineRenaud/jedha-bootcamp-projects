FROM python:3.10

WORKDIR /home/app

RUN apt-get update -y && \
    apt-get install -y nano unzip python3.10 curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://get.deta.dev/cli.sh | sh

COPY requirements.txt /dependencies/requirements.txt
RUN pip install -r /dependencies/requirements.txt

COPY . /home/app

CMD ["fastapi", "run", "main.py", "--port", "5000"]