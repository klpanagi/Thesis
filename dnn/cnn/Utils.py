#!/usr/bin/env python2

from os import path
from BaseModel import BaseModel
import json
from scipy.misc import imread, imresize
import numpy as np
from keras.preprocessing import image

_CURRENTDIR = path.abspath(__file__)
_MODELS = [
    ('vgg16', path.join(_CURRENTDIR, 'descriptors/vgg16/vgg16_model.json'))
]


def get_model_arch(modelname):
    """
    Returns the Keras Model descriptor, json object

    @type modelname: String
    @param modelname: Name of the model (vgg, )
    """
    try:
        _MODELS[modelname]
    except Exception as e:
        print 'Model {0} does not exist'.format(modelname)
        return None
    with open(_MODELS[modelname], 'r') as fstream:
        modelArch = json.load(fstream)
        return modelArch


def get_model_weights(modelname):
    """TODO: Implement to fetch from web!! """
    pass


def load_image_to_Tensor4D(fpath, tshape):
    """
    Transform an image to a Tensor4D

    @type fpath: String
    @param fpath: Path to the image file

    @type tshape: tuple
    @param tshape: The shape of the Tensor. e.g (1, 3, 400, 400)
    """
    img = image.load_img(fpath, target_size=tshape)
    tens = image.img_to_array(img)  # Create numpy array
    # (3, height, width) -> (1, 3, height, width)
    tens = np.expand_dims(tens, axis=0)
    return tens


def tensor4D_to_img(x):
    x = x[0]
    # Normalize tensor: center on 0., ensure std is 0.1
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1
    # Clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)
    # Convert to RGB array
    x *= 255
    x = x.transpose((1, 2, 0))
    x = np.clip(x, 0, 255).astype('uint8')
    return x
