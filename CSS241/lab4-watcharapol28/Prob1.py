#64090500421
import numpy as np

def f(x):
    return x**6

def diff(x, h):
    return (f(x + h) - f(x - h)) / (2*h)


def richardson_diff(x, h = 0.75, N = 2):
    t = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        t[i][0] = diff(x, h)
        for j in range(1, i + 1):
            t[i][j] = t[i][j - 1] + ((t[i][j - 1] - t[i - 1][j - 1]) / (4**j - 1))
        h /= 2
    return t[N][N]

