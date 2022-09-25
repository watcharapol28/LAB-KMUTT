#64090500421
eps = 1e-6

def f(x):
    return x**3 - 3*x + 1


def secant(xstart1, xstart2):
    # 3 root found. 0.347, -1.879, and 1.532
    #f = lambda x: x**3 - 3*x +1 
    #fprime = lambda x: 
    while abs((xstart2 - xstart1) / xstart2) > eps:
        x3 = xstart2 - (f(xstart2) * ((xstart2 - xstart1) / (f(xstart2) - f(xstart1))))
        xstart1 = xstart2
        xstart2 = x3
        #print("x1 = ",xstart1," x2 = ",xstart2," x3 = ",x3, end ='')

    return xstart2


"""def secant(xfirst, xsecond):
    xthird = xsecond - f(xsecond) * ((xsecond - xfirst) / (f(xsecond) - f(xfirst)))
    #print("x1 = ",xfirst," x2 = ",xsecond," x3 = ",xthird, end ='')
    #print()
    if np.abs((xthird - xsecond) / xthird) < eps:
        return xthird
    else:
        secant(xsecond, xthird)
"""