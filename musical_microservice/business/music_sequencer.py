import copy
from collections import deque
import json
import jmespath
import os

from musical_microservice.modules.music import *
from musical_microservice.modules.track import Track


class MusicSequencer:
    """
    This class sequences and returns chunks of audio data
    """
    def __init__(self, music_source_dir, num_steps=24):
        relative_path = os.path.join(os.getcwd(), music_source_dir)

        # load the json search index
        music_source = open(os.path.join(relative_path, 'source.json'))
        self._search_index = json.load(music_source)

        # instantiate the music objects
        self._music_map = {}
        for music in self._search_index['music']:
            wav_path = os.path.join(relative_path, music['filename'])
            music_type = music['type']

            if music_type == 'vamp':
                self._music_map[music['filename']] = Vamp(wav_path, music['parameter_annotations'])
            else:
                self._music_map[music['filename']] = Music(wav_path, music['parameter_annotations'])

        self.tracks = {'vamp': Track(num_steps)}


    def get_all_music(self):
        return copy.copy(self._music_map)


    def find_by_type(self, musicType):
        hits = jmespath.search(
            f'music[?(parameter_annotations.type == {musicType})]',
            self._search_index
        )
        return [self._music_map[hit['filename']] for hit in hits]
