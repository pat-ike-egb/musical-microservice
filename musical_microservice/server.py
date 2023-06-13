from concurrent import futures

import grpc
from services.audio_server import AudioService
from services.generated import audio_server_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add audio service endpoint to server
    audio_service = AudioService()
    audio_server_pb2_grpc.add_AudioServerServicer_to_server(audio_service, server)

    server.add_insecure_port("[::]:50051")

    server.start()

    print("now listening on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
