from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image  # lib for img loading
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image

import hw_pro
base_dir = 'hw_pro/hw_pro'  # path to data
x_train = []  # empty list for images
y_train = []  # empty list for class markers
img_height = 20  # setting img properties
img_width = 20

for patch in os.listdir(base_dir):  # enumeration of filedirs in main dir
    for img in os.listdir(base_dir + '/' + patch):  # enumerating files in file directories
        # adding img to the img list
        x_train.append(image.img_to_array(image.load_img(base_dir + '/' + patch + '/' + img,
                                                         target_size=(img_height, img_width),
                                                         color_mode='grayscale')))
        if patch == '0':  # adding 0 or 1 to the markers massive according to filename
            y_train.append(0)
        else:
            y_train.append(1)

x_train = np.array(x_train)  # converting our lists into numpy-array
y_train = np.array(y_train)
#  let's look what we got here:
print('x_train shape is:', x_train.shape)
print('y_train shape is:', y_train.shape)
