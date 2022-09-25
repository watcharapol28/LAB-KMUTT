#64090500421
eps = 1e-6

def f(x):
    return x**3 - 3*x + 1


def fprime(x):
    return 3 * x**2 - 3


def newton(xstart):
    while True :
        x = xstart
        xstart = xstart - (f(xstart) / fprime(xstart))
        #print(np.abs((xstart - x) / xstart))
        if abs((xstart - x) / xstart) < eps:
            break
        
    # 3 root found. 0.347, -1.879, and 1.532
    #f = lambda x: x**3 - 3*x +1 
    #fprime = lambda x: 
    return xstart