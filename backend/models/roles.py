from mongoengine import Document, StringField


class Roles(Document):
    nombre = StringField(unique=True)
