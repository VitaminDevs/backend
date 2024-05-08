import pprint
from os import getenv  #obtiene el vaor de la variable de entorno
from dotenv import load_dotenv 
from mongoengine import Document, StringField, DateTimeField, connect
# Coleccion "NOTICIAS"
class Noticias(Document):
    titulo = StringField(required=True)  #require=True sirve para no dejar el campo vacio (identico al "NOT NULL")
    fecha_publicacion = DateTimeField(required=True)
    fecha_modificacion = DateTimeField()
    nombre_guardado_minio = StringField()
    estado = StringField()
    usuario = StringField()
    comentario = StringField()

#Coleccion "Usuario"
class Usuario (Document): 
    nombre = StringField(required=True)
    rol = StringField (required=True)
    email = StringField (required=True)
    contraseña = StringField (required=True)
    Salt = StringField () #incriptacion de la contraseña
    noticias_publicadas = StringField ( )
    noticias_aprobadas = StringField ()
    noticias_proceso = StringField ()
    
#Coleccion "Estados"
class Estados (Document): 
    aprobas = StringField()
    revision = StringField ()
    espera = StringField ()



