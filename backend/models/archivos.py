from mongoengine import connect, Document, StringField, UUIDField, DateTimeField, ListField, ReferenceField, EmailField

class Estados(Document):
    nombre = StringField(unique=True) #nombre unico
    # estados de las noticias (proceso, pendiente, eprobada, publicada, rechazada)

class Noticias(Document):
    id = UUIDField(primary_key=True)
    titulo = StringField(required=True)
    descripcion = StringField(required=True) #ver
    fecha_publicacion = DateTimeField(required=True)
    fecha_modificacion = ListField(DateTimeField())
    estado = ReferenceField(Estados)
    autor = ReferenceField('Usuario') # esto es una ref diferida, evita errores de ref circular
    #autor = ReferenceField(Usuario, reverse_delete_rule=CASCADE)
    # EN ESTE CASO SI ELIMINAN EL USUARIO, SUS NOTICIAS SERIAN ELIMINADAS (preguntar)

class Usuario(Document):
    nombre = StringField()
    rol = StringField()
    email = EmailField()
    contraseña = StringField()
    noticias = ListField(ReferenceField(Noticias))