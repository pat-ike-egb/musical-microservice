import wave

class MusicSequencer:
    """
    This class sequences and returns audio-data
    """
    def __init__(self):
        self.music = [] # list of models.Music


    def get_next_chunk(self):
        return