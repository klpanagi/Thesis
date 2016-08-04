#!/bin/bash -ie


function _build_theano_optimized () {
  # Core deps
  sudo apt-get update
  sudo apt-get install -y python-dev
  # Python deps
  #pip install numpy scipy

  # Clone Theano Repo
  cd ~
  git clone git://github.com/Theano/Theano.git
  cd Theano
  git checkout tags/rel-0.7.1a1
  python setup.py develop --user
}


_build_theano_optimized
