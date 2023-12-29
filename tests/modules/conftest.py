import os

import pytest
from dotenv import load_dotenv
from modules.util.storage import get_object_storage_client
from moto import mock_s3

music_dir_path = os.path.join(os.path.dirname(__file__), "data")
env_file_path = os.path.join(os.path.dirname(__file__), ".env.test")


def pytest_generate_tests(metafunc):
    load_dotenv(env_file_path)


@pytest.fixture(autouse=True)
def moto_boto():
    # setup: start moto server and create the bucket
    mock = mock_s3()
    mock.start()
    client = get_object_storage_client()
    client.create_bucket(Bucket=os.environ.get("S3_BUCKET"))
    yield
    # teardown: stop moto server
    mock.stop()


@pytest.fixture
def test_recording():
    key = os.path.join(
        "musical-microservice", "opuses", "test", "recordings", "test.wav"
    )

    client = get_object_storage_client()
    client.upload_file(
        os.path.join(music_dir_path, "recordings", "test.wav"),
        os.environ.get("S3_BUCKET"),
        key,
    )
    client.close()
    return key


@pytest.fixture
def test_score():
    key = os.path.join(
        "musical-microservice", "opuses", "test_composition", "score", "test.mxl"
    )

    client = get_object_storage_client()
    client.upload_file(
        os.path.join(music_dir_path, "scores", "test.mxl"),
        os.environ.get("S3_BUCKET"),
        key,
    )
    client.close()
    return key


@pytest.fixture
def test_opus_config():
    key = os.path.join("musical-microservice", "opuses", "config.json")

    client = get_object_storage_client()
    client.upload_file(
        os.path.join(music_dir_path, "config.json"),
        os.environ.get("S3_BUCKET"),
        key,
    )
    client.close()
    return key
