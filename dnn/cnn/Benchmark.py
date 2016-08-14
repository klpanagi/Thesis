#!/usr/bin/env python2

from scipy.misc import imread, imresize
from matplotlib import pyplot as plt
import numpy as np
import time
import subprocess
import os
import json


class Benchmark(object):
    """Benchmark runner class"""

    def __init__(self, cnn_model):
        """Constructor """

        self._cnnModel = cnn_model
        self._proc = self._get_processor_family()
        self._ompThreads = self._get_OMP_NUM_THREADS()
        self._perf = None

    def _get_processor_family(self):
        command = "cat /proc/cpuinfo"
        info = subprocess.check_output(command, shell=True).strip()
        for line in info.split("\n"):
            if "model name" in line:
                print line.split(": ")[1]
                return line.split(": ")[1]

    def _get_OMP_NUM_THREADS(self):
        try:
            nT = os.environ["OMP_NUM_THREADS"]
        except KeyError:
            nT = "Unknown! Set OMP_NUM_THREADS env variable"
        return nT

    def _load_image(self, fpath):
        return imread(fpath)

    def _resize_img_to_fit_cnn(self, img):
        cnnInShape = self._get_model_input_shape()
        img = imresize(img, cnnInShape[2:])
        img = np.transpose(img, (2, 0, 1))
        # Add 4rth dimension as required to create the Tensor4D
        img = np.expand_dims(img, axis=0)
        return img

    def _get_model_input_shape(self):
        return self._cnnModel.input_shape

    def run_for_performance(self, fimg, iterations=100):
        _img = self._load_image(fimg)
        _img = self._resize_img_to_fit_cnn(_img)
        self._print_header()

        timings = []
        # First classification always takes x3 slowdown! We exclude it from
        # calculations
        self._cnnModel.classify(_img)
        for i in range(iterations):
            ts = time.time()
            out = self._cnnModel.classify(_img)
            # print np.argmax(out)
            telapsed = time.time() - ts
            timings.append(telapsed)
            print "Iteration {0}: {1} seconds".format(i, telapsed)
        tAll = sum(timings)
        tAvg = tAll / iterations
        print "{0} classifications: {1} seconds".format(iterations, tAll)
        print "Average classification time for {0} iterations: {1} seconds".format(
            iterations, tAvg)
        self._make_perf_results(timings, tAvg=tAvg, tAll=tAll)

    def _print(self, string):
        """TODO: beautify! """
        print string

    def _print_header(self):
        msg = "\n{0}Benchmark for CNN Model:{1} {2}{3}".format(
            "\033[1;34m", "\033[1;33m", self._cnnModel.name, "\033[0m")
        msg += "\n-------------------------------------"
        msg += "\n  * CPU: {0}".format(self._proc)
        msg += "\n  * OpenMP-Threads ($OMP_NUM_THREADS): {0}".format(
            self._ompThreads)
        msg += "\n-------------------------------------\n"
        print msg

    def _make_perf_results(self, timings, tAvg=None, tAll=None):
        if tAll is None:
            tAll = sum(timings)
        if tAvg is None:
            tAvg = tAll / len(timings)
        self._perf = {
            "processor": self._proc,
            "threads": self._ompThreads,
            "cnn_model": {
                "name": self._cnnModel.name,
                "num_layers": len(self._cnnModel.layers)
            },
            "timings": timings,
            "average": tAvg
        }

    def save_results(self, fpath=None):
        if fpath is None:
            fpath = "benchmark_{0}.json".format(self._cnnModel.name)
        with open(fpath, 'w') as fstream:
            json.dump(self._perf, fstream, sort_keys=False, indent=4)

    def create_figure(self, fpath=None):
        title = "Platform: {0}, Num-Threads: {1}".format(self._proc,
                                                         self._ompThreads)
        suffix = "nthreads_{0}".format(self._ompThreads)
        fig = plt.figure(1)
        fig.suptitle(title, fontsize=14)
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        ax.set_title("Performance Benchmark for {0} CNN".format(
            self._cnnModel.name))
        ax.set_xlabel("Classification iteration (discrete)")
        ax.set_ylabel("Time (secs)")
        # (0,0 is lower-left and 1,1 is upper-right)
        ax.text(0.5, 0.5, 'Average={0}'.format(self._perf["average"]),
                ha='center', va='center', transform=ax.transAxes,
                fontsize=12, color='blue')
        ax.plot(range(len(self._perf["timings"])), self._perf["timings"], 'o')
        fig.savefig('benchmark_perf_{0}.png'.format(suffix))
        plt.close(fig)
