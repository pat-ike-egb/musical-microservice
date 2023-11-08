import music21 as m21

from .instrument import Instrument, PitchRange, Roll


class String(Instrument):
    def __init__(self, name: str, pitch_range: PitchRange):
        super().__init__(name=name, pitch_range=pitch_range)
        # TODO: Add the "characteristic" of the string as described by instrumentation


class StringInstrument(Instrument):
    def __init__(self, name):
        super().__init__(name)

        # i.e. for violin, G string, D, A, E
        self.strings: Roll[String] = Roll()


class Violin(StringInstrument):
    def __init__(self, name):
        super().__init__(name=name)

        # G strings
        G_open = m21.pitch.Pitch("G3")
        G_upper = m21.pitch.Pitch("G4")
        self.strings.insert(String(G_open.name, PitchRange(G_open, G_upper)))

        D_open = m21.pitch.Pitch("D4")
        D_upper = m21.pitch.Pitch("D5")
        self.strings.insert(String(D_open.name, PitchRange(D_open, D_upper)))

        A_open = m21.pitch.Pitch("A4")
        A_upper = m21.pitch.Pitch("A5")
        self.strings.insert(String(A_open.name, PitchRange(A_open, A_upper)))

        E_open = m21.pitch.Pitch("E5")
        E_upper = m21.pitch.Pitch("E7")
        self.strings.insert(String(E_open.name, PitchRange(E_open, E_upper)))

        self.pitch_range = PitchRange(G_open, E_upper)
