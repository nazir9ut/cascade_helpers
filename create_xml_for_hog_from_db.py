from lxml import etree
from os import listdir
from os.path import isfile, join
from peewee import *
from math import floor
from mark_plates_settings import mypath
from mark_plates_settings import xml_file_path
from mark_plates_settings import xml_file
from mark_plates_settings import data_dir

from mark_plates_settings import Image












# create XML
root = etree.Element('dataset')



# another child with text
name = etree.Element('name')
name.text = 'Testing faces'
root.append(name)


comment = etree.Element('comment')
comment.text = 'These are images from the PASCAL VOC 2011 dataset.'
root.append(comment)


images = etree.Element('images')
root.append(images)







# check if table is populated with images
print Image.select().count()






img_files =  Image.select()

for file in img_files:
    image = etree.Element('image')
    image.attrib['file'] = data_dir + file.file
    images.append(image)

    # margin = (file.y3 - file.y0) / 2.0
    # width = int(floor(file.x1 - file.x0 + 2 * margin))
    # height = width / 3

    margin = (file.y3 - file.y0) / 2.0
    width = int(floor(file.x1 - file.x0))
    height = int(floor(file.y3 - file.y0))

    box = etree.Element('box')
    # box.attrib['top'] = str(int(floor(file.y0 - margin)))
    # box.attrib['left'] = str(int(floor(file.x0 - margin)))
    box.attrib['top'] = str(int(floor(file.y0)))
    box.attrib['left'] = str(int(floor(file.x0)))
    box.attrib['width'] = str(width)
    # box.attrib['height'] = str(int(floor(file.y3 - file.y0 + 2 * margin)))
    box.attrib['height'] = str(height)
    image.append(box)






# pretty string
s = etree.tostring(root, pretty_print=True)
print s




with open(xml_file_path + xml_file, 'w') as file:
    file.write("""<?xml version='1.0' encoding='ISO-8859-1'?>\n""")
    file.write("""<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>""")
    file.write("\n")
    file.write(s)