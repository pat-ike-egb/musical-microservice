import json
import os.path
import unittest

import pyaudio

from musical_microservice.modules.music import Music, Vamp


def audio_test(music: Music, max_duration: float = 20.0):
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(
        format=p.get_format_from_width(music.get_wav().getsampwidth()),
        channels=music.get_wav().getnchannels(),
        rate=music.get_wav().getframerate(),
        output=True,
    )

    # read resources
    data = music.step()
    elapsed = 0.0

    while data and (elapsed < max_duration):
        stream.write(data)

        frames = len(data) / (
            music.get_wav().getnchannels() * music.get_wav().getsampwidth()
        )
        elapsed += frames / music.get_wav().getframerate()

        data = music.step()
        print(elapsed)
        print(frames)
        print("---------------------")

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()


class MyTestCase(unittest.TestCase):
    music_dir_path = os.path.join("..", "resources", "music")
    sources = json.load(open(os.path.join(music_dir_path, "source.json")))

    def test_it_loads_music(self):
        source = self.sources["music"][0]
        path = os.path.join(self.music_dir_path, source["filename"])

        music = Music(path, source["parameter_annotations"])
        audio_test(music)
        self.assertTrue(music.complete())

    def test_it_loads_vamp(self):
        source = self.sources["music"][0]
        path = os.path.join(self.music_dir_path, source["filename"])

        music = Vamp(path, source["parameter_annotations"])
        audio_test(music, 3 * music.get_duration())
        self.assertFalse(music.complete())
        self.assertEqual(3, music.get_loops())


if __name__ == "__main__":
    unittest.main()
