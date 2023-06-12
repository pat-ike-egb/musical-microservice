import os

import generated.audio_server_pb2_grpc
from generated.audio_server_pb2 import AudioData, ConnectRequest

from musical_microservice.modules.music_sequencer import MusicSequencer


class AudioService(generated.audio_server_pb2_grpc.AudioServerServicer):
    def __init__(self):
        super().__init__()

    def connect(self, request: ConnectRequest, context):
        music_dir_path = os.path.join(os.getcwd(), "../resources/music")

        # create a new music sequencer for this connection:
        sequencer = MusicSequencer(music_dir_path)

        # audio should be buffered, perhaps it's the clients job to buffer the audio
        while True:
            yield AudioData(data=sequencer.step())
