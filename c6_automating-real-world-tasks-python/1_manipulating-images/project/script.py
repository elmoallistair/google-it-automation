#!/usr/bin/env python3

# Google IT Automation with Python Professional Certificate
# Elmo Allistair
# 11 Agu 2020

from PIL import Image
from glob import glob
import os

# Note: put this script in images folder
# Iterate through each file in the folder
for file in glob('ic_*'): # ignore hidden file (images/.DS_Store) from iteration
    image = Image.open(file).convert('RGB')
    # print(image.format, image.size, image.mode) # test
    """
    For each file:
    1. Rotate the image 90° clockwise
    2. Resize the image from 192x192 to 128x128
    3. Save the image to a new folder in .jpeg format
    """
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0] # get filename without extension
    image.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))

print('OK')