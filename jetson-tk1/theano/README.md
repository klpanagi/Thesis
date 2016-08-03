#### A few words on cuDNN dependency on CUDA version:

cuDNN depends on the version of the installed CUDA library.

- cuDNN v2 is supported for machines running CUDA 6.5 and later.
- cuDNN v3 is supported for machines running CUDA 7 and later.
- cuDNN v4 is supported for machines running CUDA 7 and later.
- cuDNN v5 is supported for machines running CUDA 7.5 and later.

#### Jetson TK1 and cuDNN version

Latest cuDNN version that can be used with Jetson TK1 board is **v2rc**. This is due the
32bit architecture and thus later supported CUDA version is **6.5**.
The trick is that CUDA 7 requires a 64-bit environment, and Jetson TK1 is 32-bit.

#### Jetson TK1 and Theano - cuDNN enabled

> cuDNN v5rc is supported in Theano master version. So it dropped cuDNN v3 support. Theano 0.8.0 and 0.8.1 support only cuDNN v3 and v4. Theano 0.8.2 will support only v4 and v5.
[Source#1](http://deeplearning.net/software/theano/library/sandbox/cuda/dnn.html)


Theano supports **cuDNN v2rc** on tags/rel-0.7.1a1. This version of Theano is used to support

#### BLAS library - Critical for speeding up (up to 10x)

[Source#1](http://theano.readthedocs.io/en/latest/install.html#troubleshooting-make-sure-you-have-a-blas-library)
[Source#2](http://theano.readthedocs.io/en/latest/install_ubuntu.html#speed-test-theano-blas)

> There are many versions of BLAS that exist and there can be up to 10x speed difference between them.

The default BLAS library that comes from the ubuntu-arm repositories is `libblas` and is a static library. **Note that this default version of BLAS is NOT optimized!!!**

There exist two more BLAS libraries that are optimized and give better performance:

- [ATLAS](http://math-atlas.sourceforge.net/): Static Library by default. Exist in Ubuntu-Arm repositories and can be installed via aptitude package manager
- [OPENBLAS](https://github.com/xianyi/OpenBLAS/tree/armv7): An **Optimized BLAS library**! Must be compiled from source!



Early Notations:

- It is prefered to build the BLAS library from source instead of picking precompiled versions as it will allow for an optimized compilation!!
- Make sure your BLAS libraries are available as dynamically-loadable libraries

- Having Theano link directly against BLAS instead of using NumPy/SciPy as an intermediate layer reduces the computational overhead. To run Theano/BLAS speed test:

```bash
$ python `python -c "import os, theano; print(os.path.dirname(theano.__file__))"`/misc/check_blas.py
```

- You can tell theano to use a different version of BLAS, in case you did not compile NumPy with a fast BLAS or if NumPy was compiled with a static library of BLAS (the latter is not supported in Theano).


##### OpenBLAS

Follow [these](https://github.com/xianyi/OpenBLAS/tree/armv7) to compile OpenBLAS libray on
Jetson TK1. Building it from source allow for accelerating based on hardware.

The after-compilation report message should be:

```bash
OpenBLAS build complete. (BLAS CBLAS LAPACK LAPACKE)

    OS               ... Linux
    Architecture     ... arm
    BINARY           ... 32bit
    C compiler       ... GCC  (command line : /usr/bin/gcc)
    Fortran compiler ... GFORTRAN  (command line : gfortran)
    Library Name     ... libopenblas_cortexa15p-r0.2.19.dev.a (Multi threaded; Max num-threads is 4)
```

#### Install Theano on a Jetson TK1 board

Simply execute the `theano_install.sh` on the Jetson TK1 board

#### Configure Theano

Copy the `theanorc` file to <jetson-tki>:~/.theanorc

**TODO**: Description on each configuration parameter


#### Initial test

Test that Theano is properly installed with cuDNN and cuBLAS enabled. Send the `cudnn_r2_test.py` script to the jetson-tk1 board and execute
