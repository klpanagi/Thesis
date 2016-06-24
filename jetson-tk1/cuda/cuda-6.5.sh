#!/bin/bash

URL="http://developer.download.nvidia.com/embedded/L4T/r21_Release_v3.0/cuda-repo-l4t-r21.3-6-5-prod_6.5-42_armhf.deb"

cd /tmp
wget ${URL}

sudo dpkg -i cuda-repo-l4t-r21.3-6-5-prod_6.5-42_armhf.deb
sudo apt-get -y update
sudo apt-get -y install cuda-toolkit-6-5

#grep -q "export PATH=.*/usr/local/cuda-6.5/bin" ~/.bashrc || echo "export PATH=/usr/local/cuda-6.5/bin:$PATH">>~/.bashrc

#grep -q "export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib" ~/.bashrc || echo "export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib:$LD_LIBRARY_PATH" >> ~/.bashrc

#source ~/.bashrc
