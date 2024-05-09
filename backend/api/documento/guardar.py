import io
import uuid
from datetime import datetime  # agregar import
from os import getenv

from flask import Blueprint, jsonify, request

from backend.database import get_minio_client, get_mongo_conection
from backend.models import Noticias

guardar_bp = Blueprint("guardar", __name__, url_prefix="/guardar")


@guardar_bp.post("")
def guardar_documento():
    metadatos = request.form.to_dict()

    # lo cambiamos por el objeto Estado leido de la DB
    # para que mongo pueda establecer la relacion entre ambos
    # metadatos["estado"] = Estados.objects(nombre=metadatos["estado"])

    if not metadatos.get("identificador", False):
        noticia = guardar_metadatos_nueva_noticia(metadatos)

    else:
        noticia = actualizar_metadatos_noticia(metadatos)

    guardar_documento_bucket(noticia.identificador)
    noticia.save()

    return jsonify(
        {
            "msg": f"noticia {noticia.titulo} guardada con exito",
            "noticia": noticia.to_json(),
        }
    )


def guardar_metadatos_nueva_noticia(metadatos):
    nueva_noticia = Noticias()

    nueva_noticia.identificador = str(uuid.uuid4())
    nueva_noticia.titulo = metadatos["titulo"]
    # nueva_noticia.fecha_publicacion = metadatos["fecha_publicacion"]
    nueva_noticia.fecha_modificacion.append(datetime.now())
    # nueva_noticia.estado = metadatos["estado"]

    return nueva_noticia


def actualizar_metadatos_noticia(metadatos):
    # si existe agrega fecha de modificacion
    # busca el obj con el ID del documento
    noticia: Noticias = Noticias.objects(identificador=metadatos["identificador"])[0]

    # agrega al arreglo nueva fecha
    noticia.fecha_modificacion.append(datetime.now())

    return noticia


def guardar_documento_bucket(identificador):
    minio_client = get_minio_client()

    raw_document = io.BytesIO(request.form["textarea"].encode("UTF-8"))
    # esta linea obtiene su tamano
    raw_document_size = raw_document.getbuffer().nbytes

    minio_client.put_object(
        getenv("DOCUMENTS_BUCKET_NAME"),
        identificador,
        raw_document,
        raw_document_size,
    )
