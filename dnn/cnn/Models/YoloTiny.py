#!/usr/bin/env python2

from os import path
from keras import backend as K
from keras.models import Model
from keras.layers import Flatten, Dense, Input
from keras.layers.convolutional import (
    Convolution2D,
    MaxPooling2D,
    ZeroPadding2D)

from BaseModel import BaseModel


__currentdir__ = path.dirname(path.realpath(__file__))


class YoloTiny(BaseModel):
    """
    Original implementation source here:
        https://github.com/fchollet/deep-learning-models/blob/master/vgg16.py
    """

    def __init__(self, classifier="voc",
                 input_shape=(3, 448, 448), **kwargs):
        """ Constructor

        Instantiate the VGG16 model architecture

        @type input_shape: Tuple
        @param input_shape: Input shape of the model (channels, height, width)

        @type include_classifier: Bool
        @param inlcude_classifier: Weather or not to inlcude the 3
            fully-connected layers, for classification, at the top of the
            network.
        """
        self._name = "YoloTiny"
        # Create the model
        super(YoloTiny, self).__init__(**kwargs)
        if classifier == "voc":
            netArch = path.join(__currentdir__, 'descriptors/yolo-tiny/modelarch_voc.json')
            weights = path.join(__currentdir__, 'weights/yolo-tiny_th_weights_voc.h5')
            self.load_arch_json(netArch)
            self.load_weights(weights)
        if classifier == "coco":
            pass
        if classifier == "imagenet":
            pass
        else:
            pass
