#!/bin/bash -ie

function _build_scipy_with_openblas() {
  #
  PREFIX=""
  CORES=4
  BLAS="openblas"
  # Deps
  pip install cython tempita

  cd ${HOME}
  git clone git://github.com/scipy/scipy.git scipy
  cd scipy
  BLAS=/opt/OpenBLAS/lib/libopenblas.so.0 LAPACK=/opt/OpenBLAS/lib/libopenblas.so.0 python setup.py install
}


_build_scipy_with_openblas
