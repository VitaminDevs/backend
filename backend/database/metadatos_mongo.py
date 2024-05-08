import pprint
from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient
from mongoengine import connect

load_dotenv("./mongo_guide/.env") #variable de entorno


PARAMETROS_CONEXION_MONGO = {
    "host": getenv("localhost"),
    "port": int(getenv("27017")),
    "username": getenv("MONGO_INITDB_ROOT_USERNAME"),
    "password": getenv("MONGO_INITDB_ROOT_PASSWORD"),
    
    # aqui definimos
    "db": getenv("MONGO_DATABASE"),
}


Noticia = {
    "titulo": "Trabajando con datos JSON en Python",
    "author": "Lucas",
    "contributors": ["Aldren", "Dan", "Joanna"],
    "url": "https://realpython.com/python-json/",
}


def get_mongo_conection():
    return connect(**PARAMETROS_CONEXION_MONGO)


