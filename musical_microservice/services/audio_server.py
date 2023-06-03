import generated.audio_server_pb2_grpc
from generated.audio_server_pb2 import (
    ConnectRequest,
    AudioData
)

class AudioService(generated.audio_server_pb2_grpc.AudioServerServicer):
    def __init__(self):
        super(AudioService, self).__init__()
        self.channels = {}

    def connect(self, request : ConnectRequest, context):
        return
