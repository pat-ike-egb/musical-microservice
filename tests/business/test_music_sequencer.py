import unittest
import json
from musical_microservice.business.music_sequencer import MusicSequencer

class MyTestCase(unittest.TestCase):
    source_path = '../data/music/index/test_source.json'
    sources = json.load(open(source_path))

    def test_it_loads_music(self):
        sequencer = MusicSequencer('../data/music/index/test_source.json')
        result =  sequencer.get_all_music()

        self.assertEqual(len(self.sources['music']), len(result))
        for music in self.sources['music']:
            self.assertIn(music['path'], result.keys())


if __name__ == '__main__':
    unittest.main()
