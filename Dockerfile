FROM python:3.10-slim-bookworm

RUN mkdir /app

COPY musical_microservice/ /app/
COPY resources/music/ /app/content/
COPY requirements.txt /app/requirements.txt

ENV CONTENT_PATH="/app/content/"

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN addgroup --gid 1001 server
RUN adduser --gid 1001 --uid 1001 server

USER 1001

EXPOSE 50051
CMD [ "python", "server.py"]
