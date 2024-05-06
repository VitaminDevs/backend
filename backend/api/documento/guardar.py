from flask import Blueprint, jsonify, request

endpoint_guardar = Blueprint("guardar", __name__, url_prefix="/guardar")


@endpoint_guardar.post("")
def save_document():

    my = "HIII"

    for l in my:
        print(l)

    return jsonify({"msg": "esto funca"}), 200
