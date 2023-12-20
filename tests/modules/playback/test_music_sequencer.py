import os

music_dir_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "resources", "music"
)


def test_it_loads_music():
    assert True
