#!/bin/bash

##
#   This script is used to flash the sample file system onto the system's internal eMMC;
##

## General Definitions ##
RELEASE="21.4.0"
L4T_Url="http://developer.download.nvidia.com/embedded/L4T/r21_Release_v4.0/Tegra124_Linux_R21.4.0_armhf.tbz2"
ROOTFS_Url="http://developer.download.nvidia.com/embedded/L4T/r21_Release_v4.0/Tegra_Linux_Sample-Root-Filesystem_R21.4.0_armhf.tbz2"
L4T_FILE="Tegra124_Linux_R21.4.0_armhf.tbz2"
ROOTFS_FILE="Tegra_Linux_Sample-Root-Filesystem_R21.4.0_armhf.tbz2"
#########################

## --------- Colors List ------------ ##
colors ()
{
  RESET='\e[0m'
  BLACK='\e[1;30m'
  RED='\e[0;31m'
  GREEN='\e[0;32m'
  YELLOW='\e[0;33m'
  BLUE='\e[0;34m'
  PURPLE='\e[0;35m'
  CYAN='\e[0;36m'
  WHITE='\e[0;37m'

  BOIBLACK='\e[1;100m'
  BRED='\e[1;31m'
  BGREEN='\e[1;32m'
  BYELLOW='\e[1;33m'
  BBLUE='\e[1;34m'
  BPURPLE='\e[1;35m'
  BCYAN='\e[1;36m'
  BWHITE='\e[1;37m'
}; colors
## --------------------------------- ##

echo -e "${BYELLOW}Flash Jetson-TK1 [bash script] ----> L4T Release ${RELEASE}${RESET}"
sleep 2

## ====================================================== ##
echo -e "\r\n${BBLUE}[Step-1]${YELLOW} Downloading and extracting L4T Release ${RELEASE}${RESET}"
mkdir -p /tmp/jetson-tk1-flash/ && cd /tmp/jetson-tk1-flash
#wget ${L4T_Url}
#wget ${ROOTFS_Url}

sudo tar xpf ${L4T_FILE}
if [ $? == 1 ]; then  # Check exit status
  exit 1
fi

cd Linux_for_Tegra/rootfs
sudo tar xpf ../../${ROOTFS_FILE}
if [ $? == 1 ]; then  # Check exit status
  exit 1
fi

cd ..
## =========================================== ##

## =========================================== ##
echo -e "\r\n${BBLUE}[Step-2]${YELLOW} Applying binaries for L4T Release ${RELEASE}${RESET}"
sleep 2
sudo ./apply_binaries.sh
## =========================================== ##


## =========================================== ##
echo -e "\r\n${BBLUE}[Step-3]${YELLOW} Flashing Jetson-TK1 with L4T Release ${RELEASE}${RESET}"
sleep 2
MSG="${BGREEN}"
MSG+="Put your Jetson-TK1 System into Recovery Mode...\r\n"
MSG+="Hold down the RECOVERY button while pressing and releasing the RESET button once on the Jetson-TK1 board.\n"
MSG+="${BRED}"
MSG+="Press [ENTER] to continue on flashing..."
MSG+="${RESET}"
echo -e ${MSG}
read cont

sudo ./flash.sh -S 14580MiB jetson-tk1 mmcblk0p1
## =========================================== ##
