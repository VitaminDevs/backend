import io
import uuid
from os import getenv

from flask import Blueprint, jsonify, request

from backend.database.documentos_minio import get_minio_client

guardar_bp = Blueprint("guardar", __name__, url_prefix="/guardar")


@guardar_bp.post("")
def guardar_documento():

    minio_client = get_minio_client()

    # minio necesita que la data del objeto
    # se halle en tipo BinaryIO y el tamaño del objeto binario
    # esta linea codifica el documento a binario UTF-8
    raw_document = io.BytesIO(request.form["textarea"].encode("UTF-8"))
    # esta linea obtiene su tamano
    raw_document_size = raw_document.getbuffer().nbytes

    # asi podriamos generar el identificador unico que usaremos en minio
    # y que debemos persistir en mongo
    identifier_name = str(uuid.uuid4())

    minio_client.put_object(
        getenv("DOCUMENTS_BUCKET_NAME"),
        identifier_name,
        raw_document,
        raw_document_size,
    )

    return jsonify({"msg": "endpoint arriba"})
