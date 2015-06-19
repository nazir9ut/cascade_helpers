import cv2
from mark_plates_settings import *


#
def draw_existing_points(row, img):
    if(row.x0 != -1 and row.y0 != -1):
        cv2.circle(img, (row.x0, row.y0), stroke, (0,255,0), stroke)
    if(row.x1 != -1 and row.y1 != -1):
        cv2.circle(img, (row.x1, row.y1), stroke, (0,255,0), stroke)
    if(row.x2 != -1 and row.y1 != -1):
        cv2.circle(img, (row.x2, row.y2), stroke, (0,255,0), stroke)
    if(row.x3 != -1 and row.y1 != -1):
        cv2.circle(img, (row.x3, row.y3), stroke, (0,255,0), stroke)