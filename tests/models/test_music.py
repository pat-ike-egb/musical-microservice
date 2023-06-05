import math
import os.path
import time
import unittest
import wave
import pyaudio

from musical_microservice.models.music import (
    Music
)

class MyTestCase(unittest.TestCase):
    def test_chunking_by_measure(self):
        path = os.path.join(os.getcwd(), '../data/music/test_vamp_1_c_major_16bit.wav')

        wav = wave.open(path, 'rb')
        print(wav.getnframes() / wav.getframerate())

        bpm = 110
        bps = bpm / 60

        print(bps)

        samples_per_beat = wav.getframerate() / bps
        samples_per_measure = 3*samples_per_beat

        print(samples_per_beat)

        p = pyaudio.PyAudio()
        #open stream
        stream = p.open(format = p.get_format_from_width(wav.getsampwidth()),
                        channels = wav.getnchannels(),
                        rate = wav.getframerate(),
                        output = True)
        #read data
        data = wav.readframes(math.floor(samples_per_measure))

        #play stream
        while data:
            stream.write(data)
            data = wav.readframes(math.floor(samples_per_measure))
            # time.sleep((1/bps))

        #stop stream
        stream.stop_stream()
        stream.close()

        #close PyAudio
        p.terminate()


if __name__ == '__main__':
    unittest.main()
