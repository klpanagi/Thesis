#!/usr/bin/env python2
import sys
# from Benchmark import Benchmark
from Models import YoloTiny
from os import path
from keras.preprocessing import image
import numpy as np


if __name__ == "__main__":
    try:
        iterations = int(sys.argv[1])
    except IndexError:
        iterations = 100

    # Create the model instance
    yolotiny = YoloTiny()
    yolotiny.compile()

    img = image.load_img('cat.jpg', target_size=(512, 512))
    img = image.crop_img(img, target_size=(448, 448))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    out = yolotiny.classify(x)
    print out
