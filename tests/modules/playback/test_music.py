from modules.playback.music import Composition


def test_it_loads_music():
    assert True


def test_it_loads_a_composition(test_recording, test_score):
    subject = Composition(test_recording, test_score)
    while not subject.complete():
        print(subject.step())
