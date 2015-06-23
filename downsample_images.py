from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image
import os



max_img_width = 1250
mypath = "/home/naz/Desktop/rects/Train/"





onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


for file in onlyfiles:
    img = Image.open(mypath + file)
    # img.show()
    # print(file)
    width = img.size[0]
    height = img.size[1]

    print(width)

    if width > max_img_width:
        print(width)
        img = img.resize((width / 2, height / 2), Image.BICUBIC)
        # print(file.split('.'))
        # img.save(mypath + file.split('.')[0] + '.jpg')
        # if(file.split('.')[1] == '.bmp'):
        #     remove(mypath + file)
        # img.show()
        # break
        img.save(mypath + file)

