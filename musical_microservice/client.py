import grpc
import pyaudio
import services.generated.audio_server_pb2 as pb2
import services.generated.audio_server_pb2_grpc as pb2_grpc

NUM_CHANNELS = 2
SAMPLE_WIDTH = 2
SAMPLES_PER_SEC = 44100

if __name__ == "__main__":
    host = "localhost"
    server_port = 50051

    # instantiate a channel
    channel = grpc.insecure_channel(f"{host}:{server_port}")

    # bind the client and the server
    stub = pb2_grpc.AudioServerStub(channel)

    request = pb2.ConnectRequest()

    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(
        format=p.get_format_from_width(SAMPLE_WIDTH),
        channels=2,
        rate=44100,
        output=True,
    )

    try:
        responses = stub.connect(request)
        for response in responses:
            print(f"Received {len(response.data)} bytes from server")
            stream.write(response.data)
    finally:
        # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()
