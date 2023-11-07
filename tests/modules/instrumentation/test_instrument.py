import music21 as m21
from modules.instrumentation.instrument import PitchRange, Tuned


def test_pitch_range_constructor():
    # todo, make C octave pitchrange fixture
    low = m21.pitch.Pitch("C4")
    high = m21.pitch.Pitch("C5")
    subject = PitchRange(low, high)

    assert subject.low == m21.pitch.Pitch("C4")
    assert subject.high == m21.pitch.Pitch("C5")


def test_tuned_constructor():
    low = m21.pitch.Pitch("C4")
    high = m21.pitch.Pitch("C5")
    pitch_range = PitchRange(low, high)

    tuned = Tuned(pitch_range)
    assert pitch_range.owner == tuned
    assert tuned.pitch_range == pitch_range
