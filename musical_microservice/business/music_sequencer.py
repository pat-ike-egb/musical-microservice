import copy
import wave
import json
import jmespath
import os

from musical_microservice.models.music import *

class MusicSequencer:
    """
    This class sequences and returns chunks of audio data

    """
    def __init__(self, music_source_dir):
        relative_path = os.path.join(os.getcwd(), music_source_dir)

        # load the json search index
        music_source = open(os.path.join(relative_path, 'source.json'))
        self._search_index = json.load(music_source)

        # instantiate the music objects
        self._music_map = {}
        for music in self._search_index['music']:
            wav_path = os.path.join(relative_path, music['filename'])
            music_type = music['type']

            if music_type == 'composition':
                self._music_map[wav_path] = Composition(wav_path, music['title'])
            else:
                self._music_map[wav_path] = Music(wav_path)

    def get_all_music(self):
        return copy.deepcopy(self._music_map)

    def find_by_key(self, key):
        hits = jmespath.search(f'music[?parameter_annotations.key_signature == {key}]', self._search_index)
        return [self._music_map[hit['path']] for hit in hits]

