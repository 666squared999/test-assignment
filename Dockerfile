FROM python:3.9-slim-buster

RUN mkdir ./app

# copy only static data needed to build
COPY ./requirements.txt ./app/requirements.txt
COPY ./scripts/docker_entry.sh ./app/entry.sh

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r requirements.txt

RUN ["chmod", "+x", "./entry.sh"]
ENTRYPOINT ["./entry.sh"]
