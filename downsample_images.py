from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image
import os


mypath = "/home/naz/Desktop/uuu/Train/"
min_width = 612


onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


for file in onlyfiles:
    img = Image.open(mypath + file)
    # img.show()
    # print(file)
    if img.size[0] > min_width:
        img = img.resize((img.size[0] / 2, img.size[1] / 2), Image.BICUBIC)
        # print(file.split('.'))
        # img.save(mypath + file.split('.')[0] + '.jpg')
        # if(file.split('.')[1] == '.bmp'):
        #     remove(mypath + file)
        # img.show()
        # break
        img.save(mypath + file)

