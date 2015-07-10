from plate_helpers import *
import cv2
import numpy as np
import mark_view_helpers



exit = False

for file in onlyfiles:
    print(file)




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
    margin_x = (row.y3 - row.y0) / 2
    margin_y = (w + 2 * margin_x - 3 * h) / 6
    cv2.rectangle(img, (x - margin_x, y - margin_y), (x + w + margin_x, y + h + margin_y), (255, 0, 255),2)






    mark_view_helpers.adjust_window(img)




    while(1):
        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xFF

        if k == 32:
            break

        if k == 27:
            exit = True
            break



    cv2.destroyWindow("img")

    if exit == True:
        break

