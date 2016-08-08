#!/bin/bash -ie


function _build_ATLAS_optimized () {
  PREFIX="/opt/ATLAS"
  CORES=""
  ATLAS_URL="https://sourceforge.net/projects/math-atlas/files/Stable/3.10.3/atlas3.10.3.tar.bz2/download"
  LAPACK_URL="http://www.netlib.org/lapack/lapack-3.6.1.tgz"
  VERSION="3.10.3"

  # Deps
  sudo apt-get install build-essential gfortran g++ gcc

  mkdir -p "${HOME}/ATLAS"
  cd "${HOME}/ATLAS"
  echo -e "\033[1;33mFetching ATLAS and NETLIB-LAPACK sources...\033[0m"
  wget ${ATLAS_URL} -O atlas3.10.3.tar.bz2  # Fetch sources
  wget ${LAPACK_URL} -O lapack-3.6.1.tgz
  bunzip2 -c atlas3.10.3.tar.bz2 | tar xfm -  # Untar
  mv ATLAS ATLAS3.10.3
  cd ATLAS3.10.3
  mkdir test-with-optimizations
  cd test-with-optimizations

  ##
  # Configuration
  ##

  # Tell ATLAS not to look for a default configuration for your system, but to build from scratch
  FLAGS="-Si archdef 0 "
  # Use the hard floating point ABI and enable NEON instructions
  FLAGS+="-D c -DATL_NONIEEE=1 -D c -DATL_ARM_HARDFP=1 -Fa alg '-mfloat-abi=hard -fPIC' "
  # Make shared/dynamic libraries
  FLAGS+="--shared "
  # Building a full LAPACK library using ATLAS and netlib's LAPACK
  FLAGS+="--with-netlib-lapack-tarfile=../../lapack-3.6.1.tgz "
  # Apply installation prefix path
  FLAGS+="--prefix=${PREFIX} "
  # Verbose
  FLAGS+="-v 2"

  echo -e "\033[1;33mATLAS configuration step with flags: ${FLAGS} ...\033[0m"
  ../configure ${FLAGS}

  ##
  # Build
  ##
  make build -j 4
}

_build_ATLAS_optimized
