#64090500421
import numpy as np


def LUdecomposition(A):
    m, n = A.shape
    U = A.copy()
    L = np.zeros_like(U)
    np.fill_diagonal(L, 1)

    # Your code here
    for i in range(n):
        for j in range(i+1, n):
            L[j, i] = U[j, i]/U[i, i]
            U[j, i:] = U[j, i:] - L[j, i]*U[i, i:]
    # end Your code

    return L, U

# Calculae Lz=b

def Lsubstitution(L, b):
    m, n = L.shape
    z = np.zeros(n, dtype=np.float64)
    
    # Your Code Here
    z[0] = b[0]/L[0, 0]

    for i in range(1, n):
        z[i] = (b[i] - np.dot(L[i, :i], z[:i]))/L[i, i]
    # End Your code
    
    return z

# Calculate Ux = z


def GaussianBacksubstitution(A, b):
    m, n = A.shape
    bn, = b.shape
    assert n == m == bn
    x = np.zeros(n, dtype=np.float64)

    # Your Code Here
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:]))/A[i, i]
    # End Your code

    return x


def Problem1(A, b):

    # Your code here.
    # 1. Calculate A=LU. Given A is known, find L,U
    L, U = LUdecomposition(A)

    # 2. Calculate Lz=b  Given L from 1., and b from the problem, find z
    z = Lsubstitution(L, b)

    # 3. Calculate Ux=z  Given U from 1., and z from 2., find x
    x = GaussianBacksubstitution(U, z)

    return x
