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

    def __eq__(self, other):
        if isinstance(other, Tempo):
            return self.beats_per_min == other.beats_per_min
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

class TimeSignature:
    def __init__(self, beats_per_measure, beat_value):
        self.beats_per_measure = beats_per_measure
        self.beat_value = beat_value

    def __eq__(self, other):
        if isinstance(other, TimeSignature):
            return self.beats_per_measure == other.beats_per_measure and self.beat_value == other.beat_value
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

class MusicalParameters:
    def __init__(self, tempo, time_signature):
        self.tempo = tempo
        self.time_signature = time_signature

    def __eq__(self, other):
        if isinstance(other, MusicalParameters):
            return self.tempo == other.tempo and self.time_signature == other.time_signature
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))