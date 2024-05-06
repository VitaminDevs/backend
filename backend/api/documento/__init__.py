from flask import Blueprint

from backend.api.documento.guardar import guardar_bp

documento_bp = Blueprint("documento", __name__, url_prefix="/documento")

documento_bp.register_blueprint(guardar_bp)
