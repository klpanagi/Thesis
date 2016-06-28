#!/bin/bash

_bgreen="\033[1;32m"
_clear="\033[0m"

VERSION="r21_2.4.10.1"
URL="http://developer.download.nvidia.com/embedded/OpenCV/L4T_21.2/libopencv4tegra-repo_l4t-r21_2.4.10.1_armhf.deb"

cd /tmp
echo -e "${_bgreen}Downloading opencv4tegra library ver: $VERSION$ ...{_clear}"
wget ${URL}

echo -e "${_bgreen}Installing opencv4tegra libs ... ${_clear}"
sudo dpkg -i libopencv4tegra-repo_l4t-r21_2.4.10.1_armhf.deb
sudo apt-get update
sudo apt-get install libopencv4tegra libopencv4tegra-dev
