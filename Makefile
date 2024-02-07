APP := musical_microservice

test:
	pytest -s

cucumber:
	@behave

.PHONY: clean generate-proto clean-generated test

generate-proto: clean-generated
	INPUT=./apis/grpc; \
	OUTPUT=./$(APP)/services/generated; \
	mkdir $$OUTPUT; \
	python3 -m grpc_tools.protoc \
		-I $$INPUT \
        --python_out=$$OUTPUT \
        --grpc_python_out=$$OUTPUT \
        $$INPUT/*.proto; \
	sed -i -E 's/^import.*_pb2/from . \0/' $$OUTPUT/*.py

clean-generated:
	rm -rf ./generated ./**/*/generated

clean: clean-generated
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml

pc:
	pre-commit run --all-files

server-start:
	python musical_microservice/server.py

client-start:
	python musical_microservice/client.py

docker-build:
	docker build . -t pat-ike-egb/musical-microservice

docker-run:
	docker run -p 50051:50051 pat-ike-egb/musical-microservice:latest
