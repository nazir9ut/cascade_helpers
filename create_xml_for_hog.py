from lxml import etree
from os import listdir
from os.path import isfile, join
from PIL import Image


# create XML
root = etree.Element('dataset')


# root.append(etree.Element('child'))

# another child with text
name = etree.Element('name')
name.text = 'Testing faces'
root.append(name)


comment = etree.Element('comment')
comment.text = 'These are images from the PASCAL VOC 2011 dataset.'
root.append(comment)


images = etree.Element('images')
root.append(images)







mypath = "/home/naz/Src/dlib-18.16/examples/plates/Train/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
    img = Image.open(mypath + file)
    # print(img.size)

    image = etree.Element('image')
    image.attrib['file'] = 'Train/' + file
    images.append(image)

    box = etree.Element('box')
    box.attrib['top'] = '220'
    box.attrib['left'] = '220'
    box.attrib['width'] = str(img.size[0] - 415)
    box.attrib['height'] = str(img.size[1] - 415)
    image.append(box)







# pretty string
s = etree.tostring(root, pretty_print=True)
print s




with open('/home/naz/Src/dlib-18.16/examples/plates/training.xml', 'w') as file:
    file.write("""<?xml version='1.0' encoding='ISO-8859-1'?>\n""")
    file.write("""<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>""")
    file.write("\n")
    file.write(s)