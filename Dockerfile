FROM python:3.10

RUN mkdir /app

COPY musical_microservice/ /app/
COPY requirements_locked.txt.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

EXPOSE 50001
ENTRYPOINT [ "python3", "-m", "musical_microservice.py"]
