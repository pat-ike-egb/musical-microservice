import grpc
import services.generated.audio_server_pb2 as pb2
import services.generated.audio_server_pb2_grpc as pb2_grpc

if __name__ == "__main__":
    host = "localhost"
    server_port = 50051

    # instantiate a channel
    channel = grpc.insecure_channel(f"{host}:{server_port}")

    # bind the client and the server
    stub = pb2_grpc.AudioServerStub(channel)

    request = pb2.ConnectRequest()

    responses: list[pb2.AudioData] = stub.connect(request)
    for response in responses:
        print(f"Hello from the server received your {len(response.data)}")
