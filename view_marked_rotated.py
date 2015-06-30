from mark_plates_settings import *
import cv2
import numpy as np
import mark_view_helpers
from math import acos
from math import sqrt
from math import degrees
from math import atan2




exit = False


for file in onlyfiles:
    # print(file)




    row = Image.select().where((Image.file == file))[0]


    img = cv2.imread(mypath + file, cv2.IMREAD_COLOR)
    img_w = img.shape[1]
    img_h = img.shape[0]



    pts = np.array([[row.x0, row.y0], [row.x1, row.y1], [row.x2, row.y2], [row.x3, row.y3]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0,255,255), 1)


    # print(row.x0, row.y0, row.x1, row.y1)


    # len1 = sqrt(row.x0 * row.x0 + row.y0 * row.y0)
    # len2 = sqrt(row.x1 * row.x1 + row.y1 * row.y1)
    #
    # dot = row.x0 * row.x1 + row.y0 * row.y1
    #
    # a = (dot * 1.0) / (len1 * len2)
    #
    # theta = acos(a)
    # print(theta)
    #
    # degree = degrees(theta)
    #
    # print(degree)


    slope = (row.y1 - row.y0) / ((row.x1 - row.x0) * 1.0)

    degree = degrees(np.arctan(slope))


    # print(degree)

    mark_view_helpers.adjust_window(img)




    M = cv2.getRotationMatrix2D((img_w/2, img_h/2), 30, 1)








    print(M)


    dst = cv2.warpAffine(img, M, (img_w, img_h))
    mark_view_helpers.adjust_window(dst, win_name = 'dst')




    M = np.append(M, [[0, 0, 1]], axis=0)

    print(np.dot(M, [187, 411, 1]))
    # [ 204.44297695  470.09807621    1.        ]







    while(1):
        cv2.imshow('img', img)
        cv2.imshow('dst', dst)


        k = cv2.waitKey(1) & 0xFF

        if k == 32:
            break

        if k == 27:
            exit = True
            break



    cv2.destroyWindow("img")

    if exit == True:
        break