from flask import Flask, g, request
from flask_cors import CORS

from backend.database import get_mongo_conection


def create_app():
    new_app_instance = Flask(__name__)
    cors_app = CORS(new_app_instance)
    new_app_instance.config["CORS_HEADERS"] = "Content-Type"
    new_app_instance.config["Access-Control-Allow-Credentials"] = "true"

    get_mongo_conection()

    @new_app_instance.route("/")
    def home_page():
        request_query = request.args
        up_message = "La API esta funcionando"
        if request_query:

            response = [up_message, "<ul>"]

            for arg, value in request_query.items():
                response.append(f"<li>{arg}: {value}</li>")

            response.append("</ul>")

            response = "".join(response)

            return response

        return up_message

    @new_app_instance.after_request
    def allow_cors(response):
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

    from backend.api import full_api

    new_app_instance.register_blueprint(full_api)

    return new_app_instance
