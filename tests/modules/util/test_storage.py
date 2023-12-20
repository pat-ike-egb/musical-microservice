import os

import pytest
from modules.util.storage import fetch_audio_recording, get_object_storage_client
from moto import mock_s3

music_dir_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "resources", "music"
)


@mock_s3
@pytest.fixture
def test_vamp():
    key = os.path.join(
        "musical-microservice", "opuses", "test_vamp", "recordings", "16bit.wav"
    )

    client = get_object_storage_client()
    client.upload_file(
        os.path.join(music_dir_path, "test_vamp.wav"),
        os.environ.get("SPACES_BUCKET"),
        key,
    )
    client.close()

    return key


@mock_s3
def test_it_fetches_audio(test_vamp):
    response = fetch_audio_recording(
        get_object_storage_client(), os.environ.get("SPACES_BUCKET"), test_vamp
    )
    print(response)
