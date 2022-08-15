import random
import numpy as np

from musical_microservice.models.musical_parameters import(
    MusicalForm, MusicalParameters, Tempo, TimeSignature
)

class MusicParameterProcessor:
    def __init__(self):
        self.tempo_by_form = {
            #TODO: you just made these up...
            MusicalForm.MINUET: (80, 109),
            MusicalForm.WALTZ : (110, 129),
            MusicalForm.SCHERZO : (130, 179)
        }

        self.time_signatures = [(3, 4), (6, 8)]

    def get_tempo(self, form) -> Tempo:
        """
        TODO
        :param form:
        :return:
        """
        if form in self.tempo_by_form: #TODO: look into better input validation practices
            low, high = self.tempo_by_form[form]
            tempo = np.random.randint(low, high)
            return Tempo(tempo)
        raise ValueError(f'{form} is not a valid musical form')
        #TODO: make a class for business-layer errors, that map to service-layer errors

    def get_time_signature(self) -> TimeSignature:
        """
        TODO
        :return:
        """
        # TODO: naive implementation that passes test
        num_beats, beat_value = self.time_signatures[0]
        return TimeSignature(num_beats, beat_value)

    def generate_musical_parameters(self, form) -> MusicalParameters:
        """
        TODO
        :param form:
        :return:
        """
        return MusicalParameters(
            self.get_tempo(form),
            self.get_time_signature()
        )
