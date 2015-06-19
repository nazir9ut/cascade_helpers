from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image as ImgLib
import cv2
from random import randint
from peewee import *
import os
from enum import Enum



mypath = "/home/naz/Desktop/rects/Train/"
img_ext = ".jpg"







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


# todo tip "not"
if not Image.table_exists():
    db.create_tables([Image])









onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


# Populate table with all images in folder using initial values
for file in onlyfiles:
    exists = Image.select().where(Image.file == file).exists()

    if not exists:
        size = ImgLib.open(mypath + file).size
        x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = -1
        width = size[0]
        height = size[1]
        Image.create(path=mypath, file=file, width = width, height = height, x0=x0, y0=y0, x1=x1, y1=y1, x2=x2, y2=y2, x3=x3 ,y3=y3)









for file in onlyfiles:

    # Skip files without specified extension
    # print(os.path.splitext(mypath + file)[1])
    if(os.path.splitext(mypath + file)[1] != img_ext):
        print("ERR: not correct extension")
        continue




    # Skip already marked images for
    rows = Image.select().where((Image.file == file) & (Image.x0 == -1) & (Image.y0 == -1))



    # this file for this coordinates is processed
    if rows.count() == 0:
        continue
    else :
        row = rows[0]





    # mouse callback function
    def draw_circle(event,x,y,flags,param):
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(img,(x,y),2,(0,0,255),2)

            global x0
            x0 = x
            global y0
            y0 = y




    img = cv2.imread(mypath + file, cv2.IMREAD_COLOR)
    cv2.namedWindow('img')
    cv2.setMouseCallback('img',draw_circle)






    while(1):
        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xFF

        if k == 32 and (-1 not in [x0, y0]) :
            # Save plate coordinates to DB
            row.x0 = x0
            row.y0 = y0
            row.save()
            print((x0, y0))
            x0 = y0 = -1
            break





    cv2.destroyWindow("img")




