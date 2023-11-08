import json
import os

from modules.playback.music import Vamp
from modules.playback.music_sequencer import MusicSequencer

music_dir_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "resources", "music"
)
sources = json.load(open(os.path.join(music_dir_path, "source.json")))

sequencer = MusicSequencer(music_dir_path)


def test_it_loads_music():
    result = sequencer.get_all_music()

    assert len(sources["music"]) == len(result)
    for music in sources["music"]:
        assert music["filename"] in result.keys()


def test_it_can_get_all_vamps():
    vamp_sources = filter(lambda source: source["type"] == "vamp", sources["music"])
    results = sequencer.find_by_type("vamp")
    assert len(list(vamp_sources)) == len(results)
    for result in results:
        assert isinstance(result, Vamp)


def test_it_can_sequence():
    sequencer.start()
    try:
        for i in range(10):
            data = sequencer.step()
            assert data
            assert len(data) > 0
    finally:
        sequencer.stop()
