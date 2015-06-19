from lxml import etree
from os import listdir
from os.path import isfile, join
from peewee import *
from math import floor


mypath = "/home/naz/Desktop/rects/Train/"
xml_file_path = "/home/naz/Desktop/rects/"
xml_file = "training.xml"
data_dir = "Train/"
# xml_file = "testing.xml"
# data_dir = "Test/"





# Database settings
db = SqliteDatabase('my_database.db', threadlocals=True)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Image(BaseModel):
    path = TextField()
    file = TextField(unique=True)
    x0 = IntegerField()
    y0 = IntegerField()
    x1 = IntegerField()
    y1 = IntegerField()
    x2 = IntegerField()
    y2 = IntegerField()
    x3 = IntegerField()
    y3 = IntegerField()




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






img_files =  Image.select().where(Image.path == mypath)

for file in img_files:
    image = etree.Element('image')
    image.attrib['file'] = data_dir + file.file
    images.append(image)

    # margin = (file.y3 - file.y0) / 2.0
    # width = int(floor(file.x1 - file.x0 + 2 * margin))
    # height = width / 3

    margin = (file.y3 - file.y0) / 2.0
    width = int(floor(file.x1 - file.x0))
    height = width / 1

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