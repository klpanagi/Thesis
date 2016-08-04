#!/bin/bash -ie

function _build_numpy_optimized () {
  # Deps
  sudo apt-get update && sudo apt-get install python-dev gfortran gcc g++

  cd ${HOME}
  git clone https://github.com/numpy/numpy  # Fetch numpy sources
  cd numpy
  git checkout v1.11.1
  cp site.cfg.example site.cfg
  # REGEX \m/
  sed -i '/\[openblas\]/{s/^\#.//;n;s/^\#.//;n;s/^\#.//;n;s/^\#.//;n;s/^\#.//}' site.cfg
  python setup.py config  # Configure
  python setup.py build --fcompiler=gnu95  # specify gfortran as the compiler
  python setup.py install --user  # Install in user space
}


_build_numpy_optimized
