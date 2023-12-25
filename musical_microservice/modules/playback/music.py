import copy
import math
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
        self.recording: AudioFile = fetch_recording(
            storage_client, os.environ.get("S3_BUCKET"), recording_key
        )
        self.score: m21.stream.Score = fetch_score(
            storage_client, os.environ.get("S3_BUCKET"), score_key
        )

        expander = m21.repeat.Expander(self.score.parts[0])
        self.playback_measures = expander.process().secondsMap

        self.current_measure = 0
        self.byte_sequences_by_measure = []
        for measure in self.playback_measures:
            data = int(self.recording.samplerate * measure["durationSeconds"])
            self.byte_sequences_by_measure.append(self.recording.read(data))

        self.recording.close()

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


class Music:
    """
    General Music file and metadata information
    """

    def __init__(self, recording_key: str):
        client = get_object_storage_client()
        bucket = os.environ.get("S3_BUCKET")
        self.audio_file = fetch_recording(client, bucket, recording_key)

        num_markers = 0

        self.current_measure = 0

        processed_samples = 0
        for i, annotation in enumerate(self.parameter_annotations):
            bps = annotation.tempo.number / 60
            samples_per_beat = self.wav.getframerate() / bps

            beats_per_measure = annotation.time_signature.beatCount
            samples_per_measure = math.ceil(samples_per_beat * beats_per_measure)

            end_of_annotation = (
                (self.parameter_annotations[i + 1].timestamp * self.wav.getframerate())
                if (i + 1 < num_markers)
                else self.wav.getnframes()
            )

            # TODO: add by measure? or add by beat?
            while processed_samples < end_of_annotation:
                measure_bytes = self.wav.readframes(samples_per_measure)
                self.byte_sequences_by_measure.append(measure_bytes)
                processed_samples = min(
                    (processed_samples + samples_per_measure), self.wav.getnframes()
                )

    def gets_all_data(self) -> list[bytes]:
        return copy.deepcopy(self.byte_sequences_by_measure)

    def get_duration(self) -> float:
        return self.wav.getnframes() / self.wav.getframerate()

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

    def get_wav(self):
        return self.wav


class Vamp(Music):
    """
    Music file meant to be seamlessly and endlessly looped
    overrides the step and is complete function
    """

    def __init__(self, recording_key):
        super().__init__(recording_key)
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


class Ornament(Music):
    """
    short, supplemental music file, triggered to play on top of a longer piece of audio
    """

    def __init__(self, recording_key):
        super().__init__(recording_key)
