#!/usr/bin/env python2

from keras.models import Model
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers import Input
from keras.layers.convolutional import (
    Convolution2D,
    MaxPooling2D,
    ZeroPadding2D)

from BaseModel import BaseModel


class VGG16(BaseModel):

    def __init__(self, input_shape=(3, 244, 244)):
        self._name = "VGG16"
        self._inLayer = Input(shape=input_shape)

        self._net = Convolution2D(64, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block1_conv1')(self._inLayer)
        self._net = Convolution2D(64, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block1_conv2')(self._net)
        self._net = MaxPooling2D((2, 2), strides=(2, 2),
                                   name='block1_pool')(self._net)

        self._net = Convolution2D(128, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block2_conv1')(self._net)
        self._net = Convolution2D(128, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block2_conv2')(self._net)
        self._net = MaxPooling2D((2, 2), strides=(2, 2),
                                   name='block2_pool')(self._net)

        self._net = Convolution2D(256, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block3_conv1')(self._net)
        self._net = Convolution2D(256, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block3_conv2')(self._net)
        self._net = Convolution2D(256, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block3_conv3')(self._net)
        self._net = MaxPooling2D((2, 2), strides=(2, 2),
                                   name='block3_pool')(self._net)

        self._net = Convolution2D(512, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block4_conv1')(self._net)
        self._net = Convolution2D(512, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block4_conv2')(self._net)
        self._net = Convolution2D(512, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block4_conv3')(self._net)
        self._net = MaxPooling2D((2, 2), strides=(2, 2),
                                   name='block4_pool')(self._net)

        self._net = Convolution2D(512, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block5_conv1')(self._net)
        self._net = Convolution2D(512, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block5_conv2')(self._net)
        self._net = Convolution2D(512, 3, 3, activation='relu',
                                    border_mode='same',
                                    name='block5_conv3')(self._net)
        self._net = MaxPooling2D((2, 2), strides=(2, 2),
                                   name='block5_pool')(self._net)


        # Classification block
        self._net = Flatten(name='flatten')(self._net)
        self._net = Dense(4096, activation='relu', name='fc1')(self._net)
        self._net = Dropout(0.5)(self._net)
        self._net = Dense(4096, activation='relu', name='fc2')(self._net)
        self._net = Dropout(0.5)(self._net)
        self._net = Dense(1000, activation='softmax', name='predictions')(
            self._net)

        # Create the model
        self._model = Model(self._inLayer, self._net)
        super(VGG16, self).__init__()


class VGG16Heatmap(VGG16):

    """VGG16 CNN Model with modifications to add heatmap option
        as proposed at:
        https://github.com/heuritech/convnets-keras
    """

    def __init__(self, **kwargs):
        super(VGG16Heatmap, self).__init__()
        self._net
        

            
