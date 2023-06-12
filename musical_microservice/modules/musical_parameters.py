import music21 as m21


class ParameterAnnotation:
    def __init__(
        self, timestamp: float, tempo: int, time_signature: str, key: dict[str, str]
    ):
        self.timestamp = timestamp
        self.tempo = m21.tempo.MetronomeMark(tempo)
        self.time_signature = m21.meter.TimeSignature(time_signature)
        self.key = m21.key.Key(key["tonic"], key["mode"])

    def __eq__(self, other):
        if isinstance(other, ParameterAnnotation):
            return (
                self.timestamp == other.timestamp
                and self.tempo == other.tempo
                and self.time_signature == other.time_signature
                and self.key == other.key
            )
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
