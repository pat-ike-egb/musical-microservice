import wave
class Music:
    """
    General Music file and metadata information
    """
    def __init__(self, wav_path):
        self.wav = wave.open(fr"{wav_path}", "rb")
        self.wav.tell()
        self.parameter_annotations = {}


class Vamp(Music):
    """
    Music file meant to be seamlessly and endlessly looped
    """
    def __init__(self, wav_path):
        super(Vamp, self).__init__(wav_path)

class Ornament(Music):
    """
    short, supplemental music file, triggered to play on top of a longer piece of audio
    """
    def __init__(self, wav_path):
        super(Ornament, self).__init__(wav_path)

class Composition(Music):
    """
    lengthy, non-repeatable body of work
    """
    def __init__(self, wav_path, title):
        super(Composition, self).__init__(wav_path)
        self.title = title