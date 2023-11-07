import copy
import math
import wave

from playback.musical_parameters import ParameterAnnotation


class Music:
    """
    General Music file and metadata information
    """

    def __init__(self, wav_path, parameter_annotations):
        self.wav = wave.open(rf"{wav_path}", "rb")
        self.parameter_annotations = [
            ParameterAnnotation(**annotation) for annotation in parameter_annotations
        ]
        self.byte_sequences_by_measure: list[bytes] = []

        self.current_measure = 0

        processed_samples = 0
        num_markers = len(self.parameter_annotations)
        print(num_markers)
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

    def __init__(self, wav_path, parameter_annotations):
        super().__init__(wav_path, parameter_annotations)
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

    def __init__(self, wav_path, parameter_annotations):
        super().__init__(wav_path, parameter_annotations)


class Composition(Music):
    """
    lengthy, non-repeatable body of work
    """

    def __init__(self, wav_path, title, parameter_annotations):
        super().__init__(wav_path, parameter_annotations)
        self.title = title
