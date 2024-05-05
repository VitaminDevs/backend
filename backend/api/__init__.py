from flask import Blueprint, jsonify


full_api = Blueprint("api", __name__, url_prefix="/api")

@full_api.get("/")
def api_is_up():
    return jsonify({"msg": "La api esta funcionando"}), 200