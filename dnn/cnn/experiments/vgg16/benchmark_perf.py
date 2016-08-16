#!/usr/bin/env python2
import sys
from Benchmark import Benchmark
from Models import VGG16
from keras import backend as K
from Utils import load_image_to_Tensor4D, tensor4D_to_img
from scipy.misc import imshow

if __name__ == "__main__":
    try:
        iterations = int(sys.argv[1])
    except IndexError:
        iterations = 100

    # Create the model instance
    vgg16 = VGG16()
    # Load weights
    vgg16.load_weights("vgg16_weights.h5")
    vgg16.compile()
    model = vgg16.get_model()
    # Generate function to visualize first layer
    convout1_f = K.function([model.layers[0].input, K.learning_phase()], [model.layers[7].output])

    _inData = load_image_to_Tensor4D('cat.jpg', (224, 224))

    # print _inData.shape

    # out = convout1_f([_inData, 0])[0]
    # print out.shape
    # convImg = tensor4D_to_img(out)
    # print convImg.shape
    # imshow(convImg[:, :, 1])

    benchmarker = Benchmark(vgg16)
    benchmarker.run_for_performance('cat.jpg', iterations=iterations)
    # benchmarker.save_results()
#     benchmarker.create_figure()
