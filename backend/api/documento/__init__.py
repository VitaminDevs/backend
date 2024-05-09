from flask import Blueprint

documento_bp = Blueprint("documento", __name__, url_prefix="/documento")


from backend.api.documento.guardar import guardar_bp

documento_bp.register_blueprint(guardar_bp)

from backend.api.documento.leer import leer_bp

documento_bp.register_blueprint(leer_bp)
