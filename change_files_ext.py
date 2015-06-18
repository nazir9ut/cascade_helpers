from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image


mypath = "/home/naz/Src/dlib-18.16/examples/plates/Train/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


for file in onlyfiles:
    img = Image.open(mypath + file)
    print(file)
    # print(file.split('.'))
    img.save(mypath + file.split('.')[0] + '.jpg')
    if(file.split('.')[1] == '.bmp'):
        remove(mypath + file)


