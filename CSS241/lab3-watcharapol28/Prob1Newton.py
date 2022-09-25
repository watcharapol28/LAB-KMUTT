#64090500421
import numpy as np


def newton(x, xi, yi):

    Table = np.zeros((len(xi), len(xi)))
    for i in range(len(xi)):
        n1 = 0
        n2 = i
        for j in range(len(xi)):
            if j >= i:
                if i == 0:
                    Table[j][i] = yi[j]
                else:
                    sum = Table[j][i-1] - Table[j-1][i-1]
                    dv = xi[n2] - xi[n1]
                    Table[j][i] = sum / dv
                n1 += 1
                n2 += 1
    ans = 0
    for i in range(len(xi)):
        if i == 0:
            ans += Table[i][i]
        else:
            sum = 1
            for j in range(i):
                sum *= x - xi[j]
            ans += Table[i][i] * sum
    return ans
