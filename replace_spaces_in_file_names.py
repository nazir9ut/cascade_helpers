from os import listdir
from os import rename
from os.path import isfile, join
import re
import os
from peewee import *




mypath = "/home/naz/Desktop/uuu/Train/"









# Database settings
db = SqliteDatabase('my_database.db', threadlocals=True)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Image(BaseModel):
    path = TextField()
    file = TextField(unique=True)
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
    # print(file)
    # print(file.count('.'))
    # if(file.count('.') > 1):
    #     print("------------------------------------")

    new_file = file.replace(" ", "")

    # ext = os.path.splitext(mypath + file)[1]
    # print(ext)
    # new_file = file.replace(".", "") + ext
    # print(new_file)
    rename(mypath + file, mypath + new_file)




img_files =  Image.select().where(Image.path == mypath)
for file in img_files:
    print(file.file)
    new_file = file.file.replace(" ", "")

    # ext = os.path.splitext(mypath + file.file)[1]
    # new_file = new_file.replace(".", "") + ext

    file.file = new_file
    file.save()

    # rename(mypath + file, mypath + new_file)



# rename("/home/naz/Desktop/ddd.txt", "/home/naz/Desktop/ddd2.txt")
