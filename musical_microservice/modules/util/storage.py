import io
import os
import tempfile

import boto3
import music21 as m21
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


def fetch_recording(client: boto3.client, bucket: str, key: str):
    get_recording_response = client.get_object(Bucket=bucket, Key=key)
    print(get_recording_response)

    return AudioFile(io.BytesIO(get_recording_response["Body"].read()))


def fetch_score(client: boto3.client, bucket: str, key: str):
    get_score_response = client.get_object(Bucket=bucket, Key=key)
    print(get_score_response)

    with tempfile.NamedTemporaryFile(suffix=".mxl", delete=False) as f_out:
        f_out.write(get_score_response["Body"].read())
        f_out.seek(0)
        f_out.close()

        assert m21.musicxml.archiveTools.uncompressMXL(f_out.name)

        # TODO: score validation...
        return m21.musicxml.xmlToM21.MusicXMLImporter().scoreFromFile(
            f'{f_out.name.split(".")[0]}.musicxml'
        )
