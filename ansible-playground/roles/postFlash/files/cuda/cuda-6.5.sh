#!/bin/bash

URL=http://developer.download.nvidia.com/embedded/L4T/r21_Release_v3.0/cuda-repo-l4t-r21.3-6-5-prod_6.5-42_armhf.deb
wget ${URL}

sudo dpkg --force-all -i cuda-repo-l4t-r21.3-6-5-prod_6.5-42_armhf.deb
sudo sed -i.bak 's/\(^deb.*main restricted\)\s*$/\1 universe multiverse/g' /etc/apt/sources.list
sudo sed -i.bak 's/\(^deb.*main restricted universe\)\s*$/\1 multiverse/g' /etc/apt/sources.list
sudo apt-get -y update
sudo apt-get -y --force-yes install cuda-toolkit-6.5 libgomp1 libfreeimage-dev libopenmpi-dev openmpi-bin
grep -q "export PATH=.*/usr/local/cuda-6.5/bin" ~/.bashrc || echo "export PATH=/usr/local/cuda-6.5/bin:$PATH">>~/.bashrc

grep -q "export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib" ~/.bashrc || echo "export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib:$LD_LIBRARY_PATH" >> ~/.bashrc

#grep -q "export __GL_PERFORM_MODE=1" ~/.bashrc || echo "export __GL_PERFORM_MODE=1"

source ~/.bashrc
