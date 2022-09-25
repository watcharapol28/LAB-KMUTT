import numpy as np

def BisectionInterest(M, L, m):    

    def bisec(f, a, b, eps):
        xm = (a + b) / 2
        if np.abs(f(xm)) < eps:
            return xm
        elif np.sign(f(a)) == np.sign(f(xm)):
            return bisec(f, xm, b, eps)
        elif np.sign(f(b)) == np.sign(f(xm)):
            return bisec(f, a, xm, eps)

    def f(r):
        return 12 * M / r * (1 - (1 + r / 12)**(-12 * m) ) - L

    xa = 0.0000001
    xb = 100.0
    epsilon = 1e-6
    xc = (bisec(f, xa, xb, epsilon))
    return xc

print(BisectionInterest(600, 150000, 30))
#64090500421
"""
def FalsePosition(M, L, m):

    def falsep(f, a, b, eps):
        while b - a < eps:
            c = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))

        if np.sign(a) == np.sign(c):
            return falsep(f, c, b, eps)

        elif np.sign(b) == np.sign(c):
            return falsep(f, a, c, eps)

    def f(r):
        return 12 * M / r * (1 - (1 + r / 12)**(-12 * m) ) - L

    xa = 0.0000001
    xb = 100.0
    epsilon = 1e-6
    xc = falsep(f, xa, xb, epsilon)
    return xc

print(FalsePosition(600, 150000, 30))
"""