import cv2
import os
import glob

# custom modules
from plate_helpers import *
import plate_settings
from plate_db import *







db_table_init()




files = glob.glob(os.path.join(plate_settings.path, '*.jpg'))





for file in files:

    path_and_file = os.path.join(plate_settings.path, file)


    # Skip already marked images for
    rows = ImageModel.select().where((ImageModel.path_and_file == path_and_file) & (ImageModel.x0 == -1) & (ImageModel.y0 == -1))



    # this file for this coordinates is processed
    if rows.count() == 0:
        continue
    else :
        row = rows[0]



    # mouse callback function
    def draw_circle(event,x,y,flags,param):
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(img,(x,y), plate_settings.stroke, (0,0,255), plate_settings.stroke)

            global x0
            x0 = x
            global y0
            y0 = y




    img = cv2.imread(path_and_file, cv2.IMREAD_COLOR)
    draw_existing_points(row, img)



    cv2.namedWindow('img')


    cv2.setMouseCallback('img',draw_circle)




    k = -1
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
            print("saving to DB")
            break

        if k == 27:
            break



    cv2.destroyWindow("img")


    if k == 27:
        break

