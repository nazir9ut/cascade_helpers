
import cv2
from random import randint
from peewee import *
import os
from enum import Enum

# custom modules
from mark_plates_settings import *
from mark_plates_helpers import draw_existing_points








for file in onlyfiles:

    # Skip files without specified extension
    # print(os.path.splitext(mypath + file)[1])
    if(os.path.splitext(mypath + file)[1] != img_ext):
        print("ERR: not correct extension")
        continue




    # Skip already marked images for
    rows = Image.select().where((Image.file == file) & (Image.x2 == -1) & (Image.y2 == -1))



    # this file for this coordinates is processed
    if rows.count() == 0:
        continue
    else :
        row = rows[0]





    # mouse callback function
    def draw_circle(event,x,y,flags,param):
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(img,(x,y),stroke ,(0,0,255), stroke)

            global x2
            x2 = x
            global y2
            y2 = y




    img = cv2.imread(mypath + file, cv2.IMREAD_COLOR)


    #
    draw_existing_points(row, img)


    cv2.namedWindow('img')
    cv2.setMouseCallback('img',draw_circle)






    while(1):
        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xFF

        if k == 32 and (-1 not in [x2, y2]) :
            # Save plate coordinates to DB
            row.x2 = x2
            row.y2 = y2
            row.save()
            print((x2, y2))
            x2 = y2 = -1
            break





    cv2.destroyWindow("img")



