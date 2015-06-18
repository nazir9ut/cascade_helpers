from os import listdir
from os.path import isfile, join
from PIL import Image



mypath = "/home/naz/Desktop/CropNumbers/Bad/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    img = Image.open(mypath + file)
    print(img.size)



with open('/home/naz/Desktop/CropNumbers/Bad.dat', 'w') as f:
    for file in onlyfiles:
        img = Image.open(mypath + file)
        f.write('Bad/' +  file + '\n')



print(onlyfiles)