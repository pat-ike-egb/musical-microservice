import os

import music21 as m21

# import music21 as m21
from modules.util.storage import fetch_recording, fetch_score, get_object_storage_client
from pedalboard.io import AudioFile


class Composition:
    """
    An audio recording with an associated music XML score
    """

    def __init__(self, recording_key, score_key):
        super().__init__()
        storage_client = get_object_storage_client()

        # fetch the audio recording from the s3 bucket
        self.recording: AudioFile = fetch_recording(
            storage_client, os.environ.get("S3_BUCKET"), recording_key
        )

        # fetch the score from the s3 bucket
        self.score: m21.stream.Score = fetch_score(
            storage_client, os.environ.get("S3_BUCKET"), score_key
        )

        # for playback purposes, expand any repeated measures
        expander = m21.repeat.Expander(self.score.parts[0])
        self.playback_measures = expander.process().secondsMap

        self.byte_sequences_by_measure = []
        for measure in self.playback_measures:
            data = int(self.recording.samplerate * measure["durationSeconds"])
            self.byte_sequences_by_measure.append(self.recording.read(data))

        self.recording.close()

        # keep track of the current measure during playback
        self.current_measure = 0

    def step(self) -> bytes | None:
        if not self.complete():
            measure = self.byte_sequences_by_measure[self.current_measure]
            self.current_measure += 1
            return measure
        return None

    def complete(self):
        return self.current_measure == len(self.byte_sequences_by_measure)

    def reset(self):
        self.current_measure = 0


class Vamp(Composition):
    """
    Music file meant to be endlessly looped.

    Rather than considering a vamp 'complete' we keep
    track of the number of loops through all of its measures

    """

    def __init__(self, recording_key, score_key):
        super().__init__(recording_key, score_key)
        self.loops = 0

    def step(self) -> bytes | None:
        measure = self.byte_sequences_by_measure[self.current_measure]
        self.current_measure += 1

        if self.current_measure >= len(self.byte_sequences_by_measure):
            self.current_measure = 0
            self.loops += 1

        return measure

    def get_loops(self):
        return self.loops

    def complete(self):
        return False
