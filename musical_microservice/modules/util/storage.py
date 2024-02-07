import io
import tempfile

import boto3
import music21 as m21
from pedalboard.io import AudioFile


def get_object_storage_client():
    session = boto3.session.Session()
    return session.client("s3")


def fetch_recording(client: boto3.client, bucket: str, key: str):
    get_recording_response = client.get_object(Bucket=bucket, Key=key)

    return AudioFile(io.BytesIO(get_recording_response["Body"].read()))


def fetch_score(client: boto3.client, bucket: str, key: str):
    get_score_response = client.get_object(Bucket=bucket, Key=key)

    with tempfile.NamedTemporaryFile(suffix=".mxl", delete=False) as f_out:
        f_out.write(get_score_response["Body"].read())
        f_out.seek(0)
        f_out.close()

        assert m21.musicxml.archiveTools.uncompressMXL(f_out.name)

        # TODO: score validation...
        return m21.musicxml.xmlToM21.MusicXMLImporter().scoreFromFile(
            f'{f_out.name.split(".")[0]}.musicxml'
        )
