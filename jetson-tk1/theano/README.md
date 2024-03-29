# Instructions on how to build **"optimized"** Theano for the NVIDIA [Jetson TK1 board](http://elinux.org/Jetson_TK1)

Here you can find instructions on how to build [Theano](https://github.com/Theano/Theano) framework to use optimized routines for the NVIDIA Jetson Tk1 board.
This work is related to work done for my Diploma Thesis.

> Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation

Theano uses [NumPy]() and/or a [BLAS]() library to perform mathematical computations on the CPU. From the other hand, on the Jetson TK1 we can also use the GPU to perform a severe of mathematical computations, using [cuDNN]()


## Theano - cuDNN enabled

cuDNN depends on the version of the installed CUDA library.

- cuDNN v2 is supported for machines running CUDA 6.5 and later.
- cuDNN v3 is supported for machines running CUDA 7 and later.
- cuDNN v4 is supported for machines running CUDA 7 and later.
- cuDNN v5 is supported for machines running CUDA 7.5 and later.


Latest cuDNN version that can be used with Jetson TK1 board is **v2rc**. This is due the
32bit architecture and thus later supported CUDA version is **6.5**.
The trick is that CUDA 7 requires a 64-bit environment, and Jetson TK1 is 32-bit.


> cuDNN v5rc is supported in Theano master version. So it dropped cuDNN v3 support. Theano 0.8.0 and 0.8.1 support only cuDNN v3 and v4. Theano 0.8.2 will support only v4 and v5.


[Source#1](http://deeplearning.net/software/theano/library/sandbox/cuda/dnn.html)

Theano supports **cuDNN v2rc** on tags/rel-0.7.1a1.


## BLAS library - Critical for speeding up (up to 10x)

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


### OpenBLAS

Follow [these](https://github.com/xianyi/OpenBLAS/tree/armv7) to compile OpenBLAS libray on
Jetson TK1. Building it from source allow for accelerating based on hardware.

Use [GNU Fortran 95 compiler (4.8)](https://gcc.gnu.org/onlinedocs/gcc-4.1.2/gfortran/) as the Fortran compiler to build openBLAS.

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

Use the `build_openBLAS_optimized.sh` script to build the OpenBLAS library as it takes into account the aforementioned optimizations.

Finally add the <path-to-openblas>/lib` path to the `LD_LIBRARY_PATH` environmental variable. OpenBLAS is installed by default in `/opt/OpenBLAS`.
To permanently do this for the user, append the following in the shellrc file, depending on the shell you are using:

```bash
$ export LD_LIBRARY_PATH=/opt/OpenBLAS/lib:$LD_LIBRARY_PATH
```

#### OpenBLAS run tests

Several test routines exist for the OpenBLAS library:

- blas-test
- lapack-test
- lapack-runtest
- lapack-timing
- tests


### ATLAS - ARM

[Source #1](http://www.vesperix.com/arm/atlas-arm/)

> The latest version of the mainline ATLAS distribution (ATLAS 3.10) includes support for ARM NEON

Pretty interesting and will will try it to compare performance with different BLAS libs, mainly OpenBLAS.

**NOTE**: Make sure you have cpu-throttoling disabled before building ATLAS ([here](http://math-atlas.sourceforge.net/atlas_install/node5.html)). To disable cpu-throttling for the Jetson TK1 board
follow [this](http://elinux.org/Jetson/Performance) guide.

##### Configure to use hard floating-point ABI, aka NEON:

```bash
$ ../configure -D c -DATL_NONIEEE=1 -D c -DATL_ARM_HARDFP=1 -Si archdef 0 -Fa alg '-mfloat-abi=hard -fPIC -mfpu=neon' --prefix=/opt/ATLAS3.10.3 --shared -v 2
```

or simply execute the script `atlas_build.sh`

## Numpy optimized for Jetson TK1

[Build-from-source](http://docs.scipy.org/doc/numpy/user/building.html)

We will build numpy using previously compiled BLAS library.

**Note**: Latest stable numpy release working on armv7 architecture is v1.11.1!!!
Chechout and build numpy at v1.11.1 tag


To get BLAS configuration information in NumPy execute:

```bash
$ python -c 'import numpy as np; numpy.__config__.show()'
```

To run the numpy tests simply execute:

```bash
$ python -c "import numpy; numpy.test()"
```


### Numpy compiled with OpenBLAS

Using OpenBLAS with numpy is way faster especially on matrix operations (multiplication, dotproduct, etc.)


To evaluate that Numpy was previously compiled with OpenBLAS simply watch at the output of:

```bash
$ python -c 'import numpy as np; numpy.__config__.show()'

lapack_opt_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['/opt/OpenBLAS/lib']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
    runtime_library_dirs = ['/opt/OpenBLAS/lib']
blas_opt_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['/opt/OpenBLAS/lib']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
    runtime_library_dirs = ['/opt/OpenBLAS/lib']
openblas_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['/opt/OpenBLAS/lib']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
    runtime_library_dirs = ['/opt/OpenBLAS/lib']
openblas_lapack_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['/opt/OpenBLAS/lib']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
    runtime_library_dirs = ['/opt/OpenBLAS/lib']
blas_mkl_info:
    NOT AVAILABLE
```


### Numpy compiled with ATLAS

### Performance tests / Benchmarks - Default blas VS optimized OpenBLAS

**Linear Algebra tests**:
 - Eighen Values
 - Single value decomposition
 - Matrix multiplication
 - Matrix dot product
 - Vector dot product
 - Matrix inversion
 - Matrix determinant

Execute the `numpy_blas_perf_tests.py` to get performance results (timings)


##### Compiled with default blas library:

```bash
$ ./numpy_blas_perf_tests.py

dotted two (1000,1000) matrices in 2602.7 ms
dotted two (4000) vectors in 11.21 us
Inversion of (1000,1000) matrix in 3420.279 ms
Determinant of (1000,1000) matrix in 972.815 ms
SVD of (2000,1000) matrix in 94.985 s
Eigendecomp of (1500,1500) matrix in 98.585 s
```

##### Compiled with OpenBLAS

```bash
$ ./numpy_blas_perf_tests.py

dotted two (1000,1000) matrices in 148.8 ms
dotted two (4000) vectors in 11.49 us
Inversion of (1000,1000) matrix in 296.545 ms
Determinant of (1000,1000) matrix in 101.563 ms
SVD of (2000,1000) matrix in 11.200 s
Eigendecomp of (1500,1500) matrix in 28.708 s
```

##### Compiled with Atlas

```bash

dotted two (1000,1000) matrices in 209.2 ms
dotted two (4000) vectors in 10.99 us
Inversion of (1000,1000) matrix in 570.630 ms
Determinant of (1000,1000) matrix in 283.391 ms
SVD of (2000,1000) matrix in 51.635 s
Eigendecomp of (1500,1500) matrix in 38.157 s
```

## Install Theano and Keras on a Jetson TK1 board

Use Theano (a29c31d3099f05991917576ef1d31cd13c33c1ca) with Keras (d745d9ee96e5d39393ac740e5b84229beca00f1d)
Using older Theano releases with current version of Keras most probably will break!!!

Simply execute the `theano_install.sh` on the Jetson TK1 board

## Configure Theano

Copy the `theanorc` file to <jetson-tki>:~/.theanorc

**TODO**: Description on each configuration parameter

