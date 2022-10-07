import math
f = lambda x: math.exp(-(x**2))


def trapezoid(f, a=0, b=1, n=60):
    h = (b - a)/n
    sum = 0
    x2 = a
    for i in range(1, n + 1):
        x1 = x2
        x2 = a + i * h
        sum += f(x1) + f(x2)
    # f is the function  f(x)
    # a is the x=a, start point of the integration
    # b is the x=b, end point of the integration
    # n means n trapezoid
    
    return sum*h/2