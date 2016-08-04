#!/bin/bash -ie

##
# OpenBLAS doesn't support g77. Please use gfortran or other Fortran compilers. e.g. make FC=gfortran.
##

function _build_openBLAS_optimized () {
  # Deps
  sudo apt-get update && sudo apt-get install gfortran build-essential gcc g++

  cd ${HOME}
  git clone git@github.com:xianyi/OpenBLAS.git  # Fetch sources
  cd OpenBLAS
  make FC=gfortran  # Build. Use gfortran compiler - GNU Fortran 95 compiler (4.8)
  sudo make PREFIX=/opt/OpenBLAS install  # Install && Set installation prefix
}


_build_openBLAS_optimized
