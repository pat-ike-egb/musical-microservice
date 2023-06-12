import threading
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
        # thread for sequencing data into tracks
        self._write_thread: threading.Thread | None = None
        self._run_sequence = False

        # load the json search index
        relative_path = os.path.join(os.getcwd(), music_source_dir)
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

    def start(self):
        self._run_sequence = True
        self._write_thread = threading.Thread(target=self._sequence)
        self._write_thread.start()

    def stop(self):
        self._run_sequence = False
        self._write_thread.join()

    def _sequence(self):
        vamps = self.find_by_type('vamp')
        vamp = vamps[0]

        track = self.tracks['vamp']
        data = vamp.step()
        while data and self._run_sequence:
            track.queue(data)
            data = vamp.step()

    def step(self):
        track = self.tracks['vamp']
        return track.step()



    def find_by_type(self, music_type: str):
        hits = jmespath.search(
            f'music[?(parameter_annotations.type == {music_type})]',
            self._search_index
        )
        return [self._music_map[hit['filename']] for hit in hits]
