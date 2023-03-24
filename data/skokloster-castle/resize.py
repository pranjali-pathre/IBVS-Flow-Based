from PIL import Image
import os, sys

path = "./"
# dirs = os.listdir( path )
dirs = [file for file in os.listdir(path) if file.endswith('.png')]

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((512,384), Image.ANTIALIAS)
            imResize.save(f + '_resized.png', quality=90)

resize()
