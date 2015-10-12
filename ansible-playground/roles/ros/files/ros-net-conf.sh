#!/bin/bash

#ETH_IP=$(ifconfig eth0 | grep "inet " | awk -F'[: ]+' '{ print $4 }')
#MASTER_IP=$(ip route | grep default | awk '{print $3}')

MASTER_PORT=11311
MASTER_HOSTNAME='master-device'  ## hostname where ROS-MASTER is running.
NODES_HOSTNAME=$(hostname)  ## Ros nodes will run on this host.

export ROS_MASTER_URI=http://${MASTER_HOSTNAME}:11311
export ROS_HOSTNAME=${NODES_HOSTNAME}

echo -e "\033[0;33mROS_MASTER_URI ---> ${ROS_MASTER_URI}\033[0m"
echo -e "\033[0;33mROS_HOSTNAME ---> ${ROS_HOSTNAME}\033[0m"
