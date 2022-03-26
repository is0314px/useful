# coding: utf-8
#from PIL import Image, ImageFilter
import numpy as np
import glob
import os
import cv2

threshold = 100 #check
paths = ['../temp/imgs',
         '../temp/imgs/a',
         '../temp/imgs/aa',
         '../temp/imgs/aaa']

for path in paths:
    for file in glob.glob(path+'/*.png'):
        img = cv2.imread(file,1)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = np.array(img).flatten()
        mean = img.mean()   

        print(file+':'+str(int(mean)))

        #"""
        if mean < threshold:
            os.remove(file)
        #"""