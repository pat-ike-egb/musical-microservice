APP := musical_microservice

test:
	PYTHONPATH=. pytest

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
        $$INPUT/musical_server.proto; \
	sed -i -E 's/^import.*_pb2/from . \0/' $$OUTPUT/*.py

#build-dev:
#
#build-prod:

clean-generated:
	rm -rf ./generated ./**/*/generated

clean: clean-generated
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
