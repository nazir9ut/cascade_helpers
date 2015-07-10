from peewee import *

# Database settings
db = SqliteDatabase('plates.db', threadlocals=True)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class ImageModel(BaseModel):
    path_and_file = TextField(unique=True)
    width = IntegerField()
    height = IntegerField()
    x0 = IntegerField()
    y0 = IntegerField()
    x1 = IntegerField()
    y1 = IntegerField()
    x2 = IntegerField()
    y2 = IntegerField()
    x3 = IntegerField()
    y3 = IntegerField()