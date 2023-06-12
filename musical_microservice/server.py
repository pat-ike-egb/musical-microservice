from concurrent import futures

import grpc

from musical_microservice.services.generated import audio_server_pb2_grpc
from musical_microservice.services.generated.audio_server_pb2_grpc import AudioServer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add audio service endpoint to server
    audio_service = AudioServer()
    audio_server_pb2_grpc.add_AudioServerServicer_to_server(audio_service, server)

    server.add_insecure_port("[::]:50051")

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
