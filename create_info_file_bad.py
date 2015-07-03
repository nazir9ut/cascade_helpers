from os import listdir
from os.path import isfile, join
from PIL import Image
from string_helpers import *


base = '/home/naz/Desktop/1_lbp'




mypath = base + "/Bad/"



remove_spaces_in_file_names(mypath)



onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    img = Image.open(mypath + file)
    print(img.size)



with open(base + '/Bad.dat', 'w') as f:
    for file in onlyfiles:
        img = Image.open(mypath + file)
        f.write('Bad/' +  file + '\n')



# print(onlyfiles)