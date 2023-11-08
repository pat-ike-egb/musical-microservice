from .instrument import Instrument


class WoodwindInstrument(Instrument):
    def __init__(self, name):
        super().__init__(name)


class Clarinet(WoodwindInstrument):
    def __init__(self, name):
        super().__init__(name)


class BbClarinet(Clarinet):
    def __init__(self, name):
        super().__init__(name)
