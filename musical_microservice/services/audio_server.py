import logging
import os
import uuid

from modules.music_sequencer import MusicSequencer
from services.generated.audio_server_pb2 import AudioData, ConnectRequest
from services.generated.audio_server_pb2_grpc import AudioServerServicer

logger = logging.getLogger("audio-service")
DEFAULT_CONTENT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "resources", "music"
)


class AudioService(AudioServerServicer):
    def __init__(self):
        super().__init__()

    def connect(self, request: ConnectRequest, context):
        stream_id = uuid.uuid4()
        logger.info(f"incoming audio streaming request, id: {stream_id}")
        content_path = os.getenv("CONTENT_PATH", DEFAULT_CONTENT_PATH)

        # create a new music sequencer for this connection:
        sequencer = MusicSequencer(content_path)
        sequencer.start()

        # audio should be buffered, perhaps it's the clients job to buffer the audio
        try:
            while True:
                data = sequencer.step()
                logger.debug(f"streaming {len(data)} bytes")
                yield AudioData(data=data)
        finally:
            logger.info(f"closing stream id: {stream_id}")
            sequencer.stop()
