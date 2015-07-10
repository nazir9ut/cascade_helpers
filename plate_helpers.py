from PIL import Image
import glob
import plate_settings
from plate_db import *
import os
import cv2




def db_table_init():
    if not ImageModel.table_exists():
        db.create_tables([ImageModel])


    files = glob.glob(os.path.join(plate_settings.path, '*.jpg'))


    # Populate table with all images in folder using initial values
    for file in files:

        path_and_file = os.path.join(plate_settings.path, file)

        exists = ImageModel.select().where(ImageModel.path_and_file == path_and_file).exists()

        if not exists:
            size = Image.open(path_and_file).size
            x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = -1
            width = size[0]
            height = size[1]


            ImageModel.create(path_and_file=path_and_file, width = width, height = height, x0=x0, y0=y0, x1=x1, y1=y1, x2=x2, y2=y2, x3=x3 ,y3=y3)






def draw_existing_points(row, img):
    stroke = plate_settings.stroke + 1


    if(row.x0 != -1 and row.y0 != -1):
        cv2.circle(img, (row.x0, row.y0), stroke, (0,255,0), stroke)
    if(row.x1 != -1 and row.y1 != -1):
        cv2.circle(img, (row.x1, row.y1), stroke, (0,255,0), stroke)
    if(row.x2 != -1 and row.y2 != -1):
        cv2.circle(img, (row.x2, row.y2), stroke, (0,255,0), stroke)
    if(row.x3 != -1 and row.y3 != -1):
        cv2.circle(img, (row.x3, row.y3), stroke, (0,255,0), stroke)





def normalize_images_size():
    files = glob.glob(os.path.join(plate_settings.path, '*.jpg'))

    for i, file in enumerate(files):
        path_and_file = os.path.join(plate_settings.path, file)

        print(path_and_file)
        print(i)

