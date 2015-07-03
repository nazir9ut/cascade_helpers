from os import listdir
from os.path import isfile, join
from PIL import Image
from string_helpers import *



base = '/home/naz/Desktop/1_haar'







mypath = base + '/Good/'




remove_spaces_in_file_names(mypath)




onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    img = Image.open(mypath + file)
    print(img.size)



with open(base + '/Good.dat', 'w') as f:
    for file in onlyfiles:
        img = Image.open(mypath + file)
        f.write('Good/' +  file + ' 1 0 0 ' + str(img.size[0]) + ' ' + str(img.size[1]) + '\n')



print(onlyfiles)