from mongoengine import Document, EmailField, ListField, ReferenceField, StringField


class Usuario(Document):
    nombre = StringField(required=True)
    rol = ReferenceField("Roles", required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    noticias = ListField(ReferenceField("Noticias"))
