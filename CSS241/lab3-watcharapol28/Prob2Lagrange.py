#64090500421
import numpy as np


def Lagrange(x, xi, yi):

    ans = 0
    for i in range(len(yi)):
        n = 1
        dv = 1
        for j in range(len(xi)):
            if i != j:
                n *= x - xi[j]
                dv *= xi[i] - xi[j]

        ans += (n / dv) * yi[i]

    return ans