#!/usr/bin/env python2
import sys
from VGG16 import VGG16
from Benchmark import Benchmark

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

    benchmarker = Benchmark(vgg16)
    benchmarker.run_for_performance('cat.jpg', iterations=iterations)
    benchmarker.save_results()
    benchmarker.create_figure()
