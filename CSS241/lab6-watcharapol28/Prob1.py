def recursive_trapezoid(f,a=0,b=1,n=60):
    h = (b - a) / 2**n
    I = f(a) + f(b)

    for i in range(1, 2**n):
        k = a + (i*h)
        I = I + 2*f(k)

    I = I * h/2

    return I
