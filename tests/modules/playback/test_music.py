from modules.playback.music import Composition
from moto import mock_s3


def test_it_loads_music():
    assert True


@mock_s3
def test_it_loads_a_composition(test_recording, test_score):
    subject = Composition(test_recording, test_score)
    print(subject)

    for p in subject.score.parts:
        print(p)
