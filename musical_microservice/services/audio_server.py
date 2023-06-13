import os

from modules.music_sequencer import MusicSequencer
from services.generated.audio_server_pb2 import AudioData, ConnectRequest
from services.generated.audio_server_pb2_grpc import AudioServerServicer


class AudioService(AudioServerServicer):
    def __init__(self):
        super().__init__()

    def connect(self, request: ConnectRequest, context):
        music_dir_path = os.path.join(os.getcwd(), "../resources/music")

        # create a new music sequencer for this connection:
        sequencer = MusicSequencer(music_dir_path)

        # audio should be buffered, perhaps it's the clients job to buffer the audio
        while True:
            yield AudioData(data=sequencer.step())
