import cv2
import numpy as np


img = cv2.imread('/home/naz/Desktop/Untitled.png', cv2.IMREAD_COLOR)


region = np.array([[187, 258], [217, 331], [576, 222], [535, 130]])



# convert to contour format
cnt = region.reshape(-1, 1, 2)
print(cnt)


# get bounding rectangle
x,y,w,h = cv2.boundingRect(cnt)



# draw rectangle
margin = 0
cv2.rectangle(img, (x - margin,y - margin), (x+w + margin, y+h + margin), (255, 0, 255),1)


cv2.imshow('win', img)
cv2.waitKey()
cv2.destroyAllWindows()