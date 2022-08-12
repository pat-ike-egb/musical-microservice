from enum import Enum

class MusicalForm(Enum):
    WALTZ = 1
    MINUET = 2
    SCHERZO = 3

class Tempo:
    def __init__(self, bpm, marking=None):
        self.beats_per_min = bpm
        if marking:
            self.marking = marking

class TimeSignature:
    def __init__(self, beats_per_measure, beat_value):
        self.beats_per_measure = beats_per_measure
        self.beat_value = beat_value

class MusicalParameters:
    def __init__(self, tempo, time_signature):
        self.tempo = tempo
        self.time_signature = time_signature