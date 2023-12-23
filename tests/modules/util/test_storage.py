import os

from modules.util.storage import fetch_recording, fetch_score, get_object_storage_client
from moto import mock_s3


@mock_s3
def test_it_fetches_recording(test_recording):
    response = fetch_recording(
        get_object_storage_client(), os.environ.get("SPACES_BUCKET"), test_recording
    )
    print(response)


@mock_s3
def test_it_fetches_score(test_score):
    response = fetch_score(
        get_object_storage_client(), os.environ.get("SPACES_BUCKET"), test_score
    )
    print(response)
