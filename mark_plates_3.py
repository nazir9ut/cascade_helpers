from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image as ImgLib
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
    if(os.path.splitext(mypath + file)[1] not in img_ext):
        print("ERR: not correct extension")
        continue


    # Skip already marked images for
    rows = Image.select().where((Image.file == file) & (Image.x3 == -1) & (Image.y3 == -1))



    # this file for this coordinates is processed
    if rows.count() == 0:
        continue
    else :
        row = rows[0]





    # mouse callback function
    def draw_circle(event,x,y,flags,param):
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(img, (x,y), stroke, (0,0,255), stroke)

            global x3
            x3 = x
            global y3
            y3 = y





    img = cv2.imread(mypath + file, cv2.IMREAD_COLOR)




    draw_existing_points(row, img)

    if(img.shape[1] > 1920):
        print("WIDTH TOO LARGE")
        aspect = 1920.0 / img.shape[1]
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 1920, int(img.shape[0] * aspect))
    elif(img.shape[0] > 1200):
        print("HEIGHT TOO LARGE")
        aspect = 1200.0 / img.shape[0]
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', int(img.shape[1] * aspect), 1200)
    else:
        print("NO RESIZE")
        cv2.namedWindow('img')

    cv2.setMouseCallback('img',draw_circle)






    while(1):
        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xFF

        if k == 32 and (-1 not in [x3, y3]) :
            # Save plate coordinates to DB
            row.x3 = x3
            row.y3 = y3
            row.save()
            print((x3, y3))
            x2 = y2 = -1
            break





    cv2.destroyWindow("img")




