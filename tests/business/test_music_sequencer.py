import unittest
import json
import os
from musical_microservice.business.music_sequencer import MusicSequencer

class MyTestCase(unittest.TestCase):
    music_dir_path = os.path.join(os.getcwd(), '../data/music')
    sources = json.load(open(os.path.join(music_dir_path, 'source.json')))

    def test_it_loads_music(self):
        sequencer = MusicSequencer(self.music_dir_path)
        result =  sequencer.get_all_music()

        self.assertEqual(len(self.sources['music']), len(result))
        for music in self.sources['music']:
            self.assertIn(music['path'], result.keys())


if __name__ == '__main__':
    unittest.main()
