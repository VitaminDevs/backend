from mongoengine import (
    DateTimeField,
    Document,
    ListField,
    ReferenceField,
    StringField,
    UUIDField,
)


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
