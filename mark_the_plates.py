from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image
import cv2
from random import randint
from peewee import *



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


# todo tip "not"
if not Image.table_exists():
    db.create_tables([Image])





mypath = "/home/naz/Desktop/uuu/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]




for file in onlyfiles:

    # Skip already marked images]
    exists = Image.select().where(Image.file == file).exists()
    if exists:
        continue




    x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = -1




    # mouse callback function
    def draw_circle(event,x,y,flags,param):

        if flags == cv2.EVENT_FLAG_LBUTTON:

            cv2.circle(img,(x,y),3,(0,0,255),3)

            global x0
            x0 = x
            global y0
            y0 = y

        elif flags == cv2.EVENT_FLAG_MBUTTON:
            cv2.circle(img,(x,y),3,(0,255,0),3)

            global x1
            x1 = x
            global y1
            y1 = y

        elif flags == (cv2.EVENT_FLAG_LBUTTON + cv2.EVENT_FLAG_CTRLKEY):
            # print(flags)
            cv2.circle(img,(x,y),3,(255,0,0),3)

            global x3
            x3 = x
            global y3
            y3 = y

        elif flags == (cv2.EVENT_FLAG_MBUTTON + cv2.EVENT_FLAG_CTRLKEY):
            cv2.circle(img,(x,y),3,(255,0,255),3)

            global x2
            x2 = x
            global y2
            y2 = y



    img = cv2.imread(mypath + file, cv2.IMREAD_COLOR)
    cv2.namedWindow('img')
    cv2.setMouseCallback('img',draw_circle)



    while(1):
        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xFF
        # print(x0, y0, x1, y1, x2, y2, x3 ,y3)

        if k == 32 and (-1 not in [x0, y0, x1, y1, x2, y2, x3 ,y3]) and y0 < y3 and y0 < y2 and y1 < y3 and y1 < y2 and x0 < x1 and x0 < x2 :
            # Save plate coordinates to DB
            Image.create(path=mypath, file=file, x0=x0, y0=y0, x1=x1, y1=y1, x2=x2, y2=y2, x3=x3 ,y3=y3)
            x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = -1
            break





    cv2.destroyWindow("img")


    # print((x0, y0), (x1, y1), (x2, y2), (x3 ,y3))

