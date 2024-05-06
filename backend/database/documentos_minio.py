from os import getenv

from minio import Minio


def get_minio_client():
    return Minio(
        getenv("MINIO_HOST"),
        access_key=getenv("MINIO_ACCESS_KEY"),
        secret_key=getenv("MINIO_SECRET_KEY"),
        secure=False,
    )
