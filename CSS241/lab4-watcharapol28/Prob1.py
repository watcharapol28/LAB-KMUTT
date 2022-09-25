def f(x):
    return x**6

def psi(x, h):
    return (f(x + h) - f(x - h)) / (2*h)

def PSI(x, h):
    return (-1 / 3 * psi(x, h)) + (4 / 3 * psi(x, h/2))

def PSI6(x,h):
    return (16/15 * PSI(x, h/2)) - (1 / 15 * PSI(x, h))

def richardson_diff(x, h=0.75, N=2):
    return PSI6(x, h)
