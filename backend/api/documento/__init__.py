from flask import Blueprint

documento_api = Blueprint("documento", __name__, url_prefix="/documento")

from backend.api.documento.guardar import endpoint_guardar

documento_api.register_blueprint(endpoint_guardar)
