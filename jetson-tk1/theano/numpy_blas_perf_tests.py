#!/usr/bin/python2.7

##
#  Source #1: https://hunseblog.wordpress.com/2014/09/15/installing-numpy-and-openblas/
#  Source #2: https://dpinte.wordpress.com/2010/01/15/numpy-performance-improvement-with-the-mkl/
##

import numpy as np
import numpy.random as npr
import time


def test_dot_two_matrices():
    """
    Test Dot product between two Matrixes of size nxn

    """
    N = 100
    n = 1000
    A = npr.randn(n, n)
    B = npr.randn(n, n)

    t = time.time()
    for i in range(N):
        C = np.dot(A, B)
    td = time.time() - t
    print("dotted two (%d,%d) matrices in %0.1f ms" % (n, n, 1e3*td/N))


def test_dot_two_vectors():
    """
    Test Dot product between two Vectors of size n

    """
    N = 100
    n = 4000

    A = npr.randn(n)
    B = npr.randn(n)

    t = time.time()
    for i in range(N):
        C = np.dot(A, B)
    td = time.time() - t
    print("dotted two (%d) vectors in %0.2f us" % (n, 1e6*td/N))


def test_matrix_inversion():
    """
    Test inversion computation of a nxn matrix

    """
    N = 100
    n = 1000

    A = npr.randn(n, n)
    t = time.time()
    for i in range(N):
        invA = np.linalg.inv(A)
    td = time.time() - t
    print("Inversion of (%d,%d) matrix in %0.3f ms" % (n, n, 1e3*td/N))


def test_matrix_determinant():
    """
    Test determinant computation of a nxn matrix

    """
    N = 100
    n = 1000

    A = npr.randn(n, n)
    t = time.time()
    for i in range(N):
        detA = np.linalg.det(A)
    td = time.time() - t
    print("Determinant of (%d,%d) matrix in %0.3f ms" % (n, n, 1e3*td/N))


def test_single_value_decomposition():
    # --- Test 3
    m, n = (2000, 1000)

    A = npr.randn(m, n)

    t = time.time()
    [U, s, V] = np.linalg.svd(A)
    [U, s, V] = np.linalg.svd(A, full_matrices=False)
    td = time.time() - t
    print("SVD of (%d,%d) matrix in %0.3f s" % (m, n, td))


def test_eighen_decomposition():
    # --- Test 4
    n = 1500
    A = npr.randn(n, n)

    t = time.time()
    w, v = np.linalg.eig(A)
    td = time.time() - t
    print("Eigendecomp of (%d,%d) matrix in %0.3f s" % (n, n, td))


if __name__ == "__main__":
    test_dot_two_matrices()
    test_dot_two_vectors()
    test_matrix_inversion()
    test_matrix_determinant()
    test_single_value_decomposition()
    test_eighen_decomposition()
