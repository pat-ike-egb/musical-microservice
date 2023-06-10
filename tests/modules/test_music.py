import os.path
import unittest
import json
import pyaudio

from musical_microservice.modules.music import (
    Music
)

class MyTestCase(unittest.TestCase):

    music_dir_path = os.path.join(os.getcwd(), '../data/music')
    sources = json.load(open(os.path.join(music_dir_path, 'source.json')))

    def test_it_loads_music(self):
        source = self.sources['music'][0]
        path = os.path.join(self.music_dir_path, source['filename'])

        music = Music(path, source['parameter_annotations'])
        wav = music.get_wav()

        p = pyaudio.PyAudio()
        #open stream
        stream = p.open(format = p.get_format_from_width(wav.getsampwidth()),
                        channels = wav.getnchannels(),
                        rate = wav.getframerate(),
                        output = True)
        #read data
        data = music.step()
        while data:
            stream.write(data)
            data = music.step()

        #stop stream
        stream.stop_stream()
        stream.close()

        #close PyAudio
        p.terminate()


if __name__ == '__main__':
    unittest.main()
