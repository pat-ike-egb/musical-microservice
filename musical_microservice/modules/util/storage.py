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

    # TODO: assert file type is audio (i.e. type.split('/')[0] == 'audio')
    return AudioFile(io.BytesIO(get_recording_response["Body"].read()))


if __name__ == "__main__":
    # Initialize a session using DigitalOcean Spaces.
    client = get_object_storage_client()
    bucket = os.environ.get("SPACES_BUCKET")
    key = os.path.join(
        "musical-microservice", "opuses", "test_opus", "recordings", "24bit.wav"
    )

    # List all buckets on your account.
    # response = client.list_objects(Bucket=bucket)
    response = fetch_audio_recording(client, bucket, key)
    print(response)
