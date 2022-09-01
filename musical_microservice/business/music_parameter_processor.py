import random
import numpy as np
import music21 as m21
from musical_microservice.models.musical_parameters import(
    MusicalForm, MusicalParameters
)

class MusicParameterProcessor:
    def __init__(self):
        self.tempo_by_form = {
            #TODO: you just made these up...
            MusicalForm.MINUET: (80, 109),
            MusicalForm.WALTZ : (110, 129),
            MusicalForm.SCHERZO : (130, 179)
        }

        self.time_signatures = ['3/4', '6/8']

    def get_tempo(self, form) -> m21.tempo.MetronomeMark:
        """
        TODO
        :param form:
        :return:
        """
        if form in self.tempo_by_form: #TODO: look into better input validation practices
            low, high = self.tempo_by_form[form]
            tempo = np.random.randint(low, high)
            return m21.tempo.MetronomeMark(number=tempo)
        raise ValueError(f'{form} is not a valid musical form')
        #TODO: make a class for business-layer errors, that map to service-layer errors

    def get_time_signature(self) -> m21.meter.TimeSignature:
        """
        TODO
        :return:
        """
        # TODO: naive implementation that passes test
        return m21.meter.TimeSignature(self.time_signatures[0])

    def generate_musical_parameters(self, form) -> MusicalParameters:
        """
        TODO
        :param form:
        :return:
        """
        return MusicalParameters(self.get_tempo(form), self.get_time_signature())
