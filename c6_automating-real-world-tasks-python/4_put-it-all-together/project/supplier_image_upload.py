#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
# image_path = os.path.expanduser('~') + '/supplier-data/images/'
image_path = 'supplier-data/images/'
jpeg_images = [image for image in os.listdir(image_path) if '.jpeg' in image]

for image in jpeg_images:
    with open(image_path+image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
