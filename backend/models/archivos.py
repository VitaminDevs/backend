from mongoengine import (
    DateTimeField,
    Document,
    EmailField,
    ListField,
    ReferenceField,
    StringField,
    UUIDField,
)


# Coleccion "NOTICIAS"
class Noticias(Document):
    identificador = UUIDField(primary_key=True)
    titulo = StringField(required=True)
    fecha_publicacion = DateTimeField(required=True)
    fecha_modificacion = ListField(DateTimeField())
    # esto es una ref diferida, evita errores de ref circular
    estado = ReferenceField("Estados")
    # se comento a autor para evitar la dependencia
    # ya que el modulo Usuarios aun no se ha desarrollado
    # autor = ReferenceField("Usuario")
    # autor = ReferenceField(Usuario, reverse_delete_rule=CASCADE)
    # EN ESTE CASO SI ELIMINAN EL USUARIO, SUS NOTICIAS SERIAN ELIMINADAS (preguntar)
    comentarios = ListField(StringField())


# Coleccion "Usuario"
class Usuario(Document):
    nombre = StringField(required=True)
    rol = ReferenceField("Roles", required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    noticias = ListField(ReferenceField("Noticias"))

