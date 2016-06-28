Build caffe with [cuDNN](https://developer.nvidia.com/cudnn) support.

> The NVIDIA CUDA® Deep Neural Network library (cuDNN) is a GPU-accelerated
> library of primitives for deep neural networks. cuDNN provides highly tuned
> implementations for standard routines such as forward and backward
> convolution, pooling, normalization, and activation layers.
> cuDNN is part of the NVIDIA Deep Learning SDK.

> Deep learning researchers and framework developers worldwide rely on cuDNN
> for high-performance GPU acceleration. It allows them to focus on training
> neural networks and developing software applications rather than spending
> time on low-level GPU performance tuning. cuDNN accelerates widely used deep
> learning frameworks, including Caffe, TensorFlow, Theano, Torch, and CNTK.
> See supported frameworks for more details.

For the NVIDIA Jetson-TK1 board, the latest supported cuDNN release is **R2**.
As caffe does not support backward compatiblitity for the cuDNN enabled implementations,
it is necessary to use a caffe fork that supports it.


##### Step#1: Clone my caffe fork repository:

```bash
git clone -b cudnn-jetsontk1 --single-branch  git@github.com:klpanagi/caffe-cudnn-jetsontk1.git
```

##### Step#2: Create the Makefile.config file:

```bash
cd caffe-cudnn-jetsontk1
cp Makefile.config.example Makefile.config
```

##### Step#3: Uncomment the following line (5) from **Makefile.config** to enable cuDNN support:

```
# USE_CUDNN := 1
```

##### Step#4: Build caffe with cuDNN support:

**Compilation with Make**:

Compilation using Make is not reccomended for using caffe in your Project.

```bash
make -j 4 all
make -j 4 runtest
```

**CMake build - (Recommended)**:

See [here](https://github.com/BVLC/caffe/pull/1667) for options and details

```bash
mkdir build && cd build
ccmake ..
make all
```

Optionally install system-wide

```bash
make install
make runtest
```
