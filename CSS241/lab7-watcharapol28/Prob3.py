#64090500421
import numpy as np

def triband(a, d, c, b):
    n = len(d)
    assert len(a) == len(c) == n-1
    assert len(b) == n

    x = np.zeros_like(b)

    # Your code here
    for i in range(1, n):
        factor = a[i-1]/d[i-1]
        d[i] = d[i] - factor*c[i-1]
        b[i] = b[i] - factor*b[i-1]
    x[n-1] = b[n-1]/d[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - c[i]*x[i+1])/d[i]
    # End your code

    return x


def Problem3(a, d, c, b):
    return triband(a, d, c, b)
