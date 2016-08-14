#!/usr/bin/bash -ie

ITERATIONS=1000
SLEEP_RATE="10m"


for nT in {1..8}
do
  OMP_NUM_THREADS=${nT} python test_classify.py ${ITERATIONS}
  # Sleep for 10 minutes to prevent overheating CPU
  echo -e "\n\033[1;33m---> Forcing to sleep for ${SLEEP_RATE} in order to prevent oveheating the CPU cores\033[0m\n"
  sleep ${SLEEP_RATE}
done
