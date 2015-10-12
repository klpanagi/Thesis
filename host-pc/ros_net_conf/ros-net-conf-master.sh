#!/bin/bash

##
#   - ROS_MASTER_URI: Tells nodes where to they can locate the ROS Master process.
#   - ROS_HOSTNAME: Sets the declared network address of a ROS Node or tool.
#
#   The master process can run on a different address than nodes, for example,
#     the roslaunch server.
#
#   Comments:
#   - ROS_MASTER_URI cannot be assigned at a public address (10.1.1.1) while ROS_HOSTNAME is defined at localhost.
#   - 
##

#ETH_IP=$(ifconfig eth1 | grep "inet " | awk -F'[: ]+' '{ print $4 }')

MASTER_PORT=11311
MASTER_HOSTNAME='master-device'
NODES_HOSTNAME='master-device'

export ROS_MASTER_URI=http://${MASTER_HOSTNAME}:${MASTER_PORT}
export ROS_HOSTNAME=${NODES_HOSTNAME}

echo -e "\033[1;32mROS_MASTER_URI ---> ${ROS_MASTER_URI}\033[0m"
echo -e "\033[1;32mROS_HOSTNAME ---> ${ROS_HOSTNAME}\033[0m"
