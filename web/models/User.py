from mongoengine import Document, StringField, DateTimeField
import datetime


class User(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
