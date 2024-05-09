from math import ceil
from os import getenv

from flask import Blueprint, jsonify, request

from backend.database import get_minio_client
from backend.models import Noticias

leer_bp = Blueprint("leer", __name__, url_prefix="/")


@leer_bp.get("<identificador>")
def leer_noticia_por_identificador(identificador):

    noticia: Noticias = None

    try:
        noticia = Noticias.objects(identificador=identificador)[0]

    except ValueError as error:
        return jsonify({"msg": "el identificador proporcionado es invalido"}), 400

    except IndexError as error:
        return (
            jsonify(
                {"msg": f"la noticia con identificador {identificador} no se hallo"}
            ),
            404,
        )

    except Exception as e:
        return jsonify({"msg": "error desconocido"}), 500

    noticia_serializada = noticia.to_mongo()
    noticia_serializada["documento"] = obtener_documento(identificador)

    return (jsonify(noticia_serializada), 200)


@leer_bp.get("")
def leer_listado_noticias():
    query_parameters = request.args

    elements_per_page = int(query_parameters.get("items", 5))
    page = int(query_parameters.get("page", 1))

    total_pages = ceil(Noticias.objects.count() / elements_per_page)

    if total_pages < 1:
        return jsonify({"msg": "No se hallaron resultados para esta búsqueda"}), 400

    if total_pages < page:
        page = total_pages

    offset = (page - 1) * elements_per_page

    noticias = Noticias.objects.skip(offset).limit(elements_per_page)

    noticias_serializadas = [n.to_mongo() for n in noticias]

    # info_respuesta = {
    #     "total_pages": total_pages,
    #     "total_noticias": Noticias.objects.count(),
    #     "current_page": page,
    #     "noticias": noticias_serializadas,
    # }

    return jsonify(noticias_serializadas), 200


def obtener_documento(identificador):

    documento = (
        get_minio_client()
        .get_object(getenv("DOCUMENTS_BUCKET_NAME"), identificador)
        .read()
        .decode("UTF-8")
    )

    return documento


def armar_consulta_noticia(query_parameters):
    """

    La idea es armar una consulta para Noticias.objects() para evitar filtrar los objetos aqui
    Noticias.objects() recibe los parametros de busqueda como llaves con valores key=value
    pero definir N combinacion de llaves=valores es sumamente impractico

    una solucion facil es generar un diccionario y agregar alli las consultas segun aparezcan en query_parameters
    por ejemplo, si query_parameters trae consigo "fecha_publicacion" podemos hacer:

    consulta = {}

    if query_parameters.get("fecha_publicacion", False):

        consulta["fecha_publicacion"] = query_parameters.get("fecha_publicacion")

    o algo por el estilo

    """

    pass
