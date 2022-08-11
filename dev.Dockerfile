FROM python:3.8

RUN mkdir /app

COPY apis/grpc/musical_server.proto /app/proto/musical_server.proto
COPY src/ /app/
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ./proto --python_out=. \
           --grpc_python_out=. ./proto/musical_server.proto \

EXPOSE 50001
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]