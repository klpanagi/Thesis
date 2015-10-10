#!/bin/bash

ETH_IP=$(ifconfig eth0 | grep "inet " | awk -F'[: ]+' '{ print $4 }')
MASTER_IP=$(ip route | grep default | awk '{print $3}')
MASTER_PORT=11311
export ROS_MASTER_URI=http://${MASTER_IP}:11311
export ROS_HOSTNAME=$(hostname)
