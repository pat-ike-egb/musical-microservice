import os

import boto3


def get_object_storage_client():
    session = boto3.session.Session()
    return session.client(
        "s3",
        region_name=os.environ.get("SPACES_REGION"),
        endpoint_url=os.environ.get("OBJECT_STORAGE_URL"),
        aws_access_key_id=os.environ.get("SPACES_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("SPACES_SECRET_KEY"),
    )


if __name__ == "__main__":
    # Initialize a session using DigitalOcean Spaces.
    client = get_object_storage_client()

    # List all buckets on your account.
    response = client.list_objects(Bucket=os.environ.get("SPACES_BUCKET"))
    print(response["Contents"])
