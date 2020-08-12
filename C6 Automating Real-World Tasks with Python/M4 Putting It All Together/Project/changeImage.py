#!/usr/bin/env python3

import os
from PIL import Image
 
# path = os.path.expanduser('~') + '/supplier-data/images/'
path = 'supplier-data/images/'
 
for file in os.listdir(path):
    if '.tiff' in file:
        
        """
        The raw images from images subdirectory contains alpha transparency layers. 
        So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. 
        Use convert("RGB") method for converting RGBA to RGB image.
        """
        
        img = Image.open(path + file).convert("RGB")
        dir, filename = os.path.split(file)
        filename = os.path.splitext(filename)[0] # get filename without extension
        
        """
        After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.
        """
        
        img.resize((600, 400)).save(path + filename + '.jpeg' , 'jpeg')