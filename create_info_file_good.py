from os import listdir
from os.path import isfile, join
from PIL import Image



mypath = "/home/naz/Desktop/CropNumbers/Good/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    img = Image.open(mypath + file)
    print(img.size)



with open('/home/naz/Desktop/CropNumbers/Good.dat', 'w') as f:
    for file in onlyfiles:
        img = Image.open(mypath + file)
        f.write('Good/' +  file + ' 1 0 0 ' + str(img.size[0]) + ' ' + str(img.size[1]) + '\n')



print(onlyfiles)