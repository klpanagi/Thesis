#!/bin/bash -ie


function _build_theano_optimized () {
  # Core deps
  sudo apt-get update
  sudo apt-get install -y python-dev
  # Python deps

  # Clone Theano Repo
  cd ~
  git clone git://github.com/Theano/Theano.git
  cd Theano
  # Tested at this commit with Keras at commit d745d9ee96e5d39393ac740e5b84229beca00f1d
  git checkout a29c31d3099f05991917576ef1d31cd13c33c1ca
  python setup.py develop --user
}


_build_theano_optimized
