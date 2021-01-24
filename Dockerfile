FROM python:3.9-slim-buster

RUN mkdir ./app
COPY ./src ./app/src
COPY ./tests ./app/tests

COPY ./requirements.txt ./app/requirements.txt
COPY ./scripts/docker_entry.sh ./app/entry.sh

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r requirements.txt
ENTRYPOINT ["./entry.sh"]
