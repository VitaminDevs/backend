from mongoengine import Document, StringField


class Estados(Document):
    nombre = StringField(unique=True)
