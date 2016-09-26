#!/usr/bin/env python2

from keras import backend as K
from keras.models import Model
from keras.layers import Flatten, Dense, Input
from keras.layers.convolutional import (
    Convolution2D,
    MaxPooling2D,
    ZeroPadding2D)

from BaseModel import BaseModel


class VGG16(BaseModel):
    """
    Original implementation source here:
        https://github.com/fchollet/deep-learning-models/blob/master/vgg16.py
    """

    def __init__(self, input_shape=(3, 244, 244), include_classifier=True,
                 **kwargs):
        """ Constructor

        Instantiate the VGG16 model architecture

        @type input_shape: Tuple
        @param input_shape: Input shape of the model (channels, height, width)

        @type include_classifier: Bool
        @param inlcude_classifier: Weather or not to inlcude the 3
            fully-connected layers, for classification, at the top of the
            network.
        """
        self._name = "VGG16"
        self._weightsUrl = {
            'th': 'https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_th_dim_ordering_th_kernels.h5',
            'tf': 'https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels.h5'
        }

        # If using the Tensor Flow backend we have to transform input shape
        if K.image_dim_ordering() == "tf":
            input_shape = (input_shape[1], input_shape[2], input_shape[0])

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
        if include_classifier:
            self._net = Flatten(name='flatten')(self._net)
            self._net = Dense(4096, activation='relu', name='fc1')(self._net)
            self._net = Dense(4096, activation='relu', name='fc2')(self._net)
            self._net = Dense(1000, activation='softmax',
                              name='predictions')(self._net)

        # Create the model
        self._model = Model(self._inLayer, self._net)
        super(VGG16, self).__init__(**kwargs)
