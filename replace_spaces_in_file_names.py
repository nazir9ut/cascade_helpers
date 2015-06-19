from os import listdir
from os import rename
from os.path import isfile, join
import re
import os
from peewee import *




mypath = "/home/naz/Desktop/uuu/Train/"









# Database settings
db = SqliteDatabase('mydb.db', threadlocals=True)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Image(BaseModel):
    path = TextField()
    file = TextField(unique=True)
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









onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    new_file = file.replace(" ", "")

    rename(mypath + file, mypath + new_file)




img_files =  Image.select()
for file in img_files:
    print(file.file)
    new_file = file.file.replace(" ", "")


    file.file = new_file
    file.save()


