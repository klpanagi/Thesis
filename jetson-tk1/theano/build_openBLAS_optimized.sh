#!/bin/bash -ie

##
# OpenBLAS doesn't support g77. Please use gfortran or other Fortran compilers. e.g. make FC=gfortran.
##

function _build_openBLAS_optimized () {
  # Vars
  PREFIX="/opt/OpenBLAS"
  CORES="4"
  RELEASE="0.2.12"

  # Deps
  sudo apt-get update && sudo apt-get install gfortran build-essential gcc g++

  cd ${HOME}
  git clone git@github.com:xianyi/OpenBLAS.git  # Fetch sources
  cd OpenBLAS
  git checkout "tags/v${RELEASE}"
  make FC=gfortran -j ${CORES}  # Build. Use gfortran compiler - GNU Fortran 95 compiler (4.8)
  sudo make PREFIX=${PREFIX} install  # Install && Set installation prefix
}


_build_openBLAS_optimized
