# coding: utf-8
from PIL import Image, ImageFilter
import numpy as np
import glob
import os

threshold = 100 #check
paths = ['imgs',
         'imgs/a',
         'imgs/aa',
         'imgs/aaa']

for path in paths:
    for file in glob.glob(path+'/*.png'):
        img = Image.open(file)
        img = img.convert('L')
        width, height = img.size

        value_list = []
        for w in range(width):
            for h in range(height):
                value = img.getpixel((w,h))
                value_list.append(value)

        value_avg = int(np.average(value_list))

        print(file+':'+str(value_avg))

        if value_avg < threshold:
            #print(file)
            os.remove(file)
