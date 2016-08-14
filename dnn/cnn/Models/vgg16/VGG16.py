#!/usr/bin/env python2

from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers.convolutional import (
    Convolution2D,
    MaxPooling2D,
    ZeroPadding2D)

from BaseModel import BaseModel


class VGG16(BaseModel):

    def __init__(self, **kwargs):
        self._name = "VGG16"
        self._model = Sequential()
        self._model.add(ZeroPadding2D((1, 1), input_shape=(3, 224, 224)))
        self._model.add(Convolution2D(64, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(64, 3, 3, activation='relu'))
        self._model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(128, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(128, 3, 3, activation='relu'))
        self._model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(256, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(256, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(256, 3, 3, activation='relu'))
        self._model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(512, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(512, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(512, 3, 3, activation='relu'))
        self._model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(512, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(512, 3, 3, activation='relu'))
        self._model.add(ZeroPadding2D((1, 1)))
        self._model.add(Convolution2D(512, 3, 3, activation='relu'))
        self._model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self._model.add(Flatten())
        self._model.add(Dense(4096, activation='relu'))
        self._model.add(Dropout(0.5))
        self._model.add(Dense(4096, activation='relu'))
        self._model.add(Dropout(0.5))
        self._model.add(Dense(1000, activation='softmax'))

        super(VGG16, self).__init__(**kwargs)
