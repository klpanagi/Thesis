#!/bin/bash -ie

# Core deps
sudo apt-get update
sudo apt-get install -y python-dev libblas-dev python-numpy python-scipy

# Python deps
#pip install numpy scipy

# Clone Theano Repo
cd ~
git clone git://github.com/Theano/Theano.git
cd Theano
git checkout tags/rel-0.7.1a1
python setup.py develop --user
