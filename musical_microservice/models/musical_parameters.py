from enum import Enum
import music21 as m21

class MusicalForm(Enum):
    WALTZ = 1
    MINUET = 2
    SCHERZO = 3

class MusicalParameters:
    def __init__(self, tempo, time_signature):
        self.tempo : m21.tempo.MetronomeMark = tempo
        self.time_signature : m21.meter.TimeSignature = time_signature

    def __eq__(self, other):
        if isinstance(other, MusicalParameters):
            return self.tempo == other.tempo and self.time_signature == other.time_signature
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))