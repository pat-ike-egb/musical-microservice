import unittest
from musical_microservice.business.music_parameter_processor import MusicParameterProcessor
from musical_microservice.models.musical_parameters import (
    MusicalForm, Tempo, TimeSignature, MusicalParameters
)

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.subject = MusicParameterProcessor()

    def test_get_tempo_returns_error_if_form_is_invalid(self):
        self.assertRaises(ValueError, self.subject.get_tempo, 'not-a-musical-form')


if __name__ == '__main__':
    unittest.main()
