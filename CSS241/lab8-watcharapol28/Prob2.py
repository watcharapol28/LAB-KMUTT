#64090500421
import numpy as np

def Jacobi(A,b,kmax):
    n, = b.shape
    x = np.zeros_like(b)

    #Your code here
    for _ in range(kmax):
        for i in range(n):
            x[i] = (b[i] - sum(A[i, j]*x[j]
                    for j in range(n) if j != i))/A[i, i]
    #end your code
    
    return x
            

def Problem2(A,b):
    return Jacobi(A,b,21)

