import os

from modules.util.storage import fetch_recording, fetch_score, get_object_storage_client


def test_it_fetches_recording(test_recording):
    response = fetch_recording(
        get_object_storage_client(), os.environ.get("S3_BUCKET"), test_recording
    )
    assert response


def test_it_fetches_score(test_score):
    response = fetch_score(
        get_object_storage_client(), os.environ.get("S3_BUCKET"), test_score
    )
    assert response
