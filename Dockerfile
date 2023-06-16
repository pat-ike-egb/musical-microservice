FROM python:3.10-slim-bookworm

RUN mkdir /app

COPY musical_microservice/ /app/
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 50001
ENTRYPOINT [ "python", "server.py"]
