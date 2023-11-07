import json
import os
import unittest

from modules.playback.music import Vamp
from modules.playback.music_sequencer import MusicSequencer


class MyTestCase(unittest.TestCase):
    music_dir_path = os.path.join(
        os.path.dirname(__file__), "..", "..", "resources", "music"
    )
    sources = json.load(open(os.path.join(music_dir_path, "source.json")))

    sequencer = MusicSequencer(music_dir_path)

    def test_it_loads_music(self):
        result = self.sequencer.get_all_music()

        self.assertEqual(len(self.sources["music"]), len(result))
        for music in self.sources["music"]:
            self.assertIn(music["filename"], result.keys())

    def test_it_can_get_all_vamps(self):
        vamp_sources = filter(
            lambda source: source["type"] == "vamp", self.sources["music"]
        )
        results = self.sequencer.find_by_type("vamp")
        self.assertEqual(len(list(vamp_sources)), len(results))
        for result in results:
            self.assertTrue(isinstance(result, Vamp))

    def test_it_can_sequence(self):
        self.sequencer.start()
        try:
            for i in range(10):
                data = self.sequencer.step()
                self.assertIsNotNone(data)
                self.assertGreater(len(data), 0)
        finally:
            self.sequencer.stop()


if __name__ == "__main__":
    unittest.main()
