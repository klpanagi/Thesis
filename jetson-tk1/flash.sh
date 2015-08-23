#!/bin/bash

##
#   This script is used to flash the sample file system onto the system's internal eMMC;
##

RELEASE="21.4.0"
L4T_Url="http://developer.download.nvidia.com/embedded/L4T/r21_Release_v4.0/Tegra124_Linux_R21.4.0_armhf.tbz2"
ROOTFS_Url="http://developer.download.nvidia.com/embedded/L4T/r21_Release_v4.0/Tegra_Linux_Sample-Root-Filesystem_R21.4.0_armhf.tbz2"
L4T_FILE="Tegra124_linux_R21.4.0_armhf.tbz2"
ROOTFS_FILE="Tegra_Linux_Sample-Root-Filesystem_R21.4.0_armhf.tbz2"


echo -e "\033[1;32mFlash Jetson-TK1 ----> L4T Release ${RELEASE}"

mkdir -p /tmp/jetson-tk1-flash/
wget ${L4T_Url}
wget ${ROOTFS_Url}
tar xpf ${ROOTFS_FILE}
tar xpf ${L4T_FILE}
