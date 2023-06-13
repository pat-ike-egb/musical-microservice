APP := musical_microservice

test:
	pytest

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

start:
	python musical_microservice/server.py
