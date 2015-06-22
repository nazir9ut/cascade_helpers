from mark_plates_settings import *
import cv2
import numpy as np



for file in onlyfiles:
    row = Image.select().where((Image.file == file))[0]


    img = cv2.imread(mypath + file, cv2.IMREAD_COLOR)


    pts = np.array([[row.x0, row.y0],[row.x1, row.y1],[row.x2, row.y2], [row.x3, row.y3]], np.int32)
    pts = pts.reshape((-1,1,2))
    # img = cv2.polylines(img,[pts],True,(0,255,255), 2)


    region = np.array([[row.x0, row.y0],[row.x1, row.y1],[row.x2, row.y2], [row.x3, row.y3]], np.int32)

    # convert to contour format
    cnt = region.reshape(-1, 1, 2)



    # get bounding rectangle
    x,y,w,h = cv2.boundingRect(cnt)


    # draw rectangle
    margin_x = 20
    margin_y = 10
    cv2.rectangle(img, (x - margin_x, y - margin_y), (x+w + margin_x, y+h + margin_y), (255, 0, 255),1)






    if(img.shape[1] > 1920):
        print("WIDTH TOO LARGE")
        aspect = 1920.0 / img.shape[1]
        cv2.namedWindow('win', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('win', 1920, int(img.shape[0] * aspect))
    elif(img.shape[0] > 1200):
        print("HEIGHT TOO LARGE")
        aspect = 1200.0 / img.shape[0]
        cv2.namedWindow('win', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('win', int(img.shape[1] * aspect), 1200)
    else:
        print("NO RESIZE")
        cv2.namedWindow('win')




    while(1):
        cv2.imshow('win',img)
        k = cv2.waitKey(1) & 0xFF

        if k == 32:
            break





    cv2.destroyWindow("win")

