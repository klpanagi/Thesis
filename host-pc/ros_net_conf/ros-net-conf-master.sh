#!/bin/bash

ETH_IP=$(ifconfig eth1 | grep "inet " | awk -F'[: ]+' '{ print $4 }')
MASTER_PORT=11311
export ROS_MASTER_URI=http://${ETH_IP}:${MASTER_PORT}
export ROS_IP=${ETH_IP}
echo -e "\033[1;32mROS_MASTER_URI ---> ${ROS_MASTER_URI}\033[0m"
echo -e "\033[1;32mROS_IP ---> ${ROS_IP}\033[0m"
