import io
import uuid
from os import getenv

from flask import Blueprint, jsonify, request

from backend.database.documentos_minio import get_minio_client

leer_bp = Blueprint("leer", __name__, url_prefix="/<identificador>")


@leer_bp.get("")
def leer_documento(identificador):

    minio_client = get_minio_client()

    identifier_name = identificador

    response = minio_client.get_object(
        getenv("DOCUMENTS_BUCKET_NAME"),
        identifier_name,
    )

    document_content = response.read().decode("UTF-8")

    return jsonify({"identificador": document_content})
