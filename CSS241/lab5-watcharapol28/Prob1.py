def trapezoid(f,a=0,b=1,n =60):
    h = (b - a)/n
    sum = 0
    x2 = a
    for i in range(1, n + 1):
        x1 = x2
        x2 = a + i * h
        sum += f(x1) + f(x2)
    
    return sum*h/2
   

