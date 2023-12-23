import os

import pytest
from dotenv import load_dotenv
from modules.util.storage import get_object_storage_client
from moto import mock_s3

music_dir_path = os.path.join(os.path.dirname(__file__), "data")


def pytest_generate_tests(metafunc):
    load_dotenv()


@pytest.fixture
def object_bucket():
    return os.environ.get("SPACES_BUCKET")


@mock_s3
@pytest.fixture
def test_recording(object_bucket):
    key = os.path.join(
        "musical-microservice", "opuses", "test", "recordings", "test.wav"
    )

    client = get_object_storage_client()
    client.upload_file(
        os.path.join(music_dir_path, "recordings", "test.wav"),
        object_bucket,
        key,
    )
    client.close()
    return key


@mock_s3
@pytest.fixture
def test_score(object_bucket):
    key = os.path.join(
        "musical-microservice", "opuses", "test_composition", "score", "test.mxl"
    )

    client = get_object_storage_client()
    client.upload_file(
        os.path.join(music_dir_path, "scores", "test.mxl"),
        object_bucket,
        key,
    )
    client.close()
    return key
