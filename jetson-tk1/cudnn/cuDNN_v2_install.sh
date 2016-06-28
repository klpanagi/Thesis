#!/bin/bash

## Execute this script on Jetson TK1 machine. The cuDNN tarball must exist in the same directory before executing

# Make sure this is executing as root
if [ $(id -u) != 0 ]; then
  echo "This script requires root permissions"
  echo "$ sudo "$0""
  exit
fi

# Untar the archive
tar -zxvf cudnn-6.5-linux-ARMv7-v2.tgz
cd cudnn-6.5-linux-ARMv7-v2
# copy the include file
cp cudnn.h /usr/local/cuda-6.5/include
cp libcudnn* /usr/local/cuda-6.5/lib
