import unittest
from musical_microservice.business.music_parameter_processor import MusicParameterProcessor
from musical_microservice.models.musical_parameters import (
    MusicalForm, MusicalParameters
)
import music21 as m21

class MusicaParameterProcessorTests(unittest.TestCase):
    def setUp(self):
        self.subject = MusicParameterProcessor()

    def test_get_tempo_returns_error_if_form_is_invalid(self):
        self.assertRaises(ValueError, self.subject.get_tempo, 'not-a-musical-form')

    def test_get_tempo_returns_valid_tempo_for_minuet(self):
        form = MusicalForm.MINUET
        # TODO: pull these out into a test constants class
        expected_low = 80
        expected_high = 109

        # TODO: a better way to make this test deterministic. Random.seed?
        for i in range(1000):
            actual = self.subject.get_tempo(form).number
            self.assertGreaterEqual(actual, expected_low)
            self.assertLessEqual(actual, expected_high)

    def test_get_tempo_returns_valid_tempo_for_waltz(self):
        form = MusicalForm.WALTZ
        # TODO: pull these out into a test constants class
        expected_low = 110
        expected_high = 129

        # TODO: a better way to make this test deterministic. Random.seed?
        for i in range(1000):
            actual = self.subject.get_tempo(form).number
            self.assertGreaterEqual(actual, expected_low)
            self.assertLessEqual(actual, expected_high)

    def test_get_tempo_returns_valid_tempo_for_scherzo(self):
        form = MusicalForm.SCHERZO
        # TODO: pull these out into a test constants class
        expected_low = 130
        expected_high = 179

        # TODO: a better way to make this test deterministic. Random.seed?
        for i in range(1000):
            actual = self.subject.get_tempo(form).number
            self.assertGreaterEqual(actual, expected_low)
            self.assertLessEqual(actual, expected_high)

    def test_get_time_signature_returns(self):
        expected = ['3/4', '6/8']
        actual = self.subject.get_time_signature().ratioString
        self.assertIn(actual, expected)

    def test_generate_musical_parameters_returns(self):
        # TODO: write a better test :(
        form = MusicalForm.SCHERZO
        expected_tempo_low = 130
        expected_tempo_high = 179
        expected_time_signatures = ['3/4', '6/8']

        actual : MusicalParameters = self.subject.generate_musical_parameters(form)
        self.assertIn(actual.time_signature.ratioString, expected_time_signatures)
        self.assertGreaterEqual(actual.tempo.number, expected_tempo_low)
        self.assertLessEqual(actual.tempo.number, expected_tempo_high)





if __name__ == '__main__':
    unittest.main()
