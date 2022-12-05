#64090500421
import numpy as np
# You may or may not use numpy

def Jacobi(A, b, kmax=20):
    n, = b.shape
    x = np.zeros_like(b)
    for _ in range(kmax):
        for i in range(n):
            x[i] = (b[i] - sum(A[i, j]*x[j]
                    for j in range(n) if j != i))/A[i, i]
    return x


def Problem2(x, xi, yi):
    # Natural Cubic Spline
    # Your code here
    ti = np.array(xi)
    h = np.diff(ti)
    b = np.diff(yi)/h

    u = [2*(h[i]+h[i+1]) for i in range(len(h)-1)]
    v = [6*(b[i+1]-b[i]) for i in range(len(b)-1)]

    eql = np.zeros((len(xi), len(xi)))

    sol = [0, *v, 0]

    eql[0][0] = 1
    eql[-1][-1] = 1

    for i in range(1, len(xi)-1):
        eql[i][i-1] = h[i-1]
        eql[i][i] = u[i-1]
        eql[i][i+1] = h[i]

    zi = Jacobi(np.array(eql), np.array(sol))

    ans = 0
    for i in range(len(xi)-1):
        if xi[i] <= x <= xi[i+1]:
            ans = zi[i+1]/(6*h[i])*(x-xi[i])**3 - zi[i]/(6*h[i]) * (x-xi[i+1])**3 + \
                (yi[i+1]/h[i] - zi[i+1]*h[i]/6)*(x-xi[i]) - \
                (yi[i]/h[i] - zi[i]*h[i]/6)*(x-xi[i+1])
            break

    return ans
