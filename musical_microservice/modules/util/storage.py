import io
import os

import boto3
from pedalboard.io import AudioFile


def get_object_storage_client():
    session = boto3.session.Session()
    return session.client(
        "s3",
        region_name=os.environ.get("SPACES_REGION"),
        endpoint_url=os.environ.get("OBJECT_STORAGE_URL"),
        aws_access_key_id=os.environ.get("SPACES_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("SPACES_SECRET_KEY"),
    )


def fetch_audio_recording(client: boto3.client, bucket: str, key: str):
    get_recording_response = client.get_object(Bucket=bucket, Key=key)
    print(get_recording_response)

    return AudioFile(io.BytesIO(get_recording_response["Body"].read()))
