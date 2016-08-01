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
[Source](http://deeplearning.net/software/theano/library/sandbox/cuda/dnn.html)


Theano supports **cuDNN v2rc** on tags/rel-0.7.1a1. This version of Theano is used to support


#### Install Theano on a Jetson TK1 board

Simply execute the `theano_install.sh` on the Jetson TK1 board

#### Configure Theano

Copy the `theanorc` file to <jetson-tki>:~/.theanorc

**TODO**: Description on each configuration parameter


#### Initial test

Test that Theano is properly installed with cuDNN and cuBLAS enabled. Send the `cudnn_r2_test.py` script to the jetson-tk1 board and execute
