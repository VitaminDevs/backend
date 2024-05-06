from os import getenv

from mongoengine import connect

PARAMETROS_CONEXION_MONGO = {
    "host": getenv("MONGO_HOST"),
    "port": int(getenv("MONGO_PORT")),
    "username": getenv("MONGO_INITDB_ROOT_USERNAME"),
    "password": getenv("MONGO_INITDB_ROOT_PASSWORD"),
    # aqui definimos
    "db": getenv("MONGO_DATABASE"),
}


def get_mongo_conection():
    return connect(**PARAMETROS_CONEXION_MONGO)
