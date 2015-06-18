from os import listdir
from os import rename
from os.path import isfile, join
import re

mypath = "/home/naz/Desktop/CropNumbers/Bad/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    # print(file)
    # print(file.count('.'))
    # if(file.count('.') > 1):
    #     print("------------------------------------")

    new_file = file.replace(" ", "")
    # print(new_file)
    rename(mypath + file, mypath + new_file)




# rename("/home/naz/Desktop/ddd.txt", "/home/naz/Desktop/ddd2.txt")
