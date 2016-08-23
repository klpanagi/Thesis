#!/usr/bin/env python2

from copy import deepcopy
from keras.models import (
    model_from_json,
    model_from_yaml,
    load_model)
from keras.utils.visualize_util import plot
from keras.optimizers import SGD
import yaml
import json
# import theano


class BaseModel(object):
    """
    Keras Model Base class
    """
    def __init__(self, name="", fpath_model="", fpath_model_arch="",
                 fpath_model_weights="", verb=2):
        """
        Constructor

        @type name: String
        @param name: Name this DNN

        @type fpath_model: String
        @param fpath_model: Keras Model HDF5 file to load.

        @type fpath_model_arch: String
        @param fpath_model_arch: Keras Model architecture file to load.
            Overwritten by fpath_model!

        @type fpath_model_weights: String
        @param fpath_model_weights Keras model weights file to load
            Overwritten by fpath_model!
        """
        super(BaseModel, self).__init__()

        if name != "":
            self._name = name
        if fpath_model != "":
            self.load_model(fpath_model)
        elif fpath_model_arch != "":
            if self._is_json_file(fpath_model_arch):
                self.load_arch_json(fpath_model_arch)
            elif self._is_yaml_file(fpath_model_arch):
                self.load_arch_yaml(fpath_model_arch)
            else:
                print "".join("Could not load keras model architecture from ",
                              fpath_model_arch)
        if fpath_model_weights != "" and self._model is not None:
            self.load_weights(fpath_model_weights)

    def get_model(self):
        """
        Return a reference to the Keras Model
        """
        return self._model

    def get_model_copy(self):
        """
        Returns a deep copy of the Keras Model
        """
        return deepcopy(self._model)

    def save_arch_json(self, fpath=""):
        """
        Saves the Model's architecture ONLY, in a json file

        @type fpath: String
        @param fpath: File path to store the model's architecture
        """
        if fpath == "":
            fpath = "".join((self._name, "_modelarch.json"))
        modelJson = self._model.to_json()
        with open(fpath, 'w') as f:
            f.write(modelJson)

    def save_arch_yaml(self, fpath=""):
        """
        Saves the Model's architecture ONLY, in a yaml file

        @type fpath: String
        @param fpath: File path to store the model's architecture
        """
        if fpath == "":
            fpath = "".join((self._name, "_modelarch.yaml"))
        modelYaml = self._model.to_yaml()
        with open(fpath, 'w') as f:
            f.write(modelYaml)

    def save_model_all(self, fpath):
        """
        Saves Keras Model into a single HDF5 file which will contain:
            - The architecture of the model, allowing to re-create it
            - The Weighjson error pythonts of the model
            - The training configuration(loss, optimizer)
            - The state of the optimizer, allowing to resume training
                exactly where you left off
        """
        if fpath == "":
            fpath = "".join((self._name, "_model.h5"))
        self._model.save(fpath)

    def load_model(self, fpath):
        """
        Load complete model from HDF5 file

        @type fpath: String
        @param fpath: Path to the hdf5 file of the model
        """
        self._model = load_model(fpath)

    def load_arch_yaml(self, fpath=""):
        """
        Load the architecture of the Keras Model from yaml file

        @type fpath: String
        @param fpath: Path to the yaml file that describes the Keras Model arch
        """
        self._model = model_from_yaml(fpath)

    def load_arch_json(self, fpath=""):
        """
        Load the architecture of the Keras Model from json file

        @type fpath: String
        @param fpath: Path to the json file that describes the Keras Model arch
        """
        self._model = model_from_json(fpath)

    def save_weights(self, fpath=""):
        """
        Store the weights of the Keras Model
        """
        if fpath == "":
            fpath = "".join((self._name, "_model.yaml"))
        self._model.save_weights(fpath)

    def load_weights(self, fpath):
        """
        Load and apply model weights from HDF5 file

        @type fpath: String
        @param fpath: Path to the hdf5 file that containes the model weights
        """
        self._model.load_weights(fpath)

    def make_graph(self, shapes=True, layer_names=True, fpath=""):
        if fpath == "":
            fpath = "".join((self._name, "_model.png"))
        plot(self._model, to_file=fpath, show_shapes=shapes,
             show_layer_names=layer_names)

    def classify(self, img):
        return self._model.predict(img)

    def compile(self, optimizer=None, loss="categorical_crossentropy",
                metrics=[]):
        """
        Configures the learning process
        """
        if optimizer is None:
            optimizer = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
        self._model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def _is_yaml_file(self, fpath):
        """
        Evaluate if a file is a proper yaml file

        @type fpath: String
        @param fpath: The file path
        """
        with open(fpath, 'r') as fstream:
            try:
                yaml.load(fstream)
            except yaml.YAMLError:
                return False
            return True

    def _is_json_file(self, fpath):
        """
        Evaluate if a file is a proper json  file

        @type fpath: String
        @param fpath: The file path
        """
        with open(fpath, 'r') as fstream:
            try:
                json.load(fstream)
            except ValueError:
                return False
            return True

    @property
    def input_shape(self):
        """
        Returns the input shape of the First Layer.

        @returns tuple
        """
        return self._model.layers[0].input_shape

    @property
    def name(self):
        return self._name

    @property
    def layers(self):
        return self._model.layers
