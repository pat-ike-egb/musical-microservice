import wave
from musical_microservice.models.musical_parameters import *
class Music:
    """
    General Music file and metadata information
    """
    def __init__(self, wav_path, parameter_annotations):
        self.wav = wave.open(fr"{wav_path}", "rb")

        self.parameter_annotations = [ParameterAnnotation(**annotation) for annotation in parameter_annotations]
        for anno in self.parameter_annotations:
            print(anno.timestamp)
            print(anno.tempo)
            print(anno.time_signature)
            print(anno.key)

        self.byte_sequences_by_measure = []

class Vamp(Music):
    """
    Music file meant to be seamlessly and endlessly looped
    """
    def __init__(self, wav_path, parameter_annotations):
        super(Vamp, self).__init__(wav_path, parameter_annotations)

class Ornament(Music):
    """
    short, supplemental music file, triggered to play on top of a longer piece of audio
    """
    def __init__(self, wav_path, parameter_annotations):
        super(Ornament, self).__init__(wav_path, parameter_annotations)

class Composition(Music):
    """
    lengthy, non-repeatable body of work
    """
    def __init__(self, wav_path, title, parameter_annotations):
        super(Composition, self).__init__(wav_path, parameter_annotations)
        self.title = title