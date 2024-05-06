from os import getenv

from flask import Blueprint, jsonify, request

guardar_bp = Blueprint("guardar", __name__, url_prefix="/guardar")


@guardar_bp.post("")
def guardar_documento():
    return jsonify({"msg": "endpoint arriba"})
