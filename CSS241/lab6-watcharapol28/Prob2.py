import numpy

def romberg( f, a, b, n ):
    r = numpy.array( [[0] * (n+1)] * (n+1), float )
    h = b - a
    r[0,0] = (h / 2) * ( f( a ) + f( b ) )
    power2 = 1
    for i in range( 1, n + 1 ):
        h = 0.5 * h
        sum = 0.0
        power2 = 2 * power2
        for k in range( 1, power2, 2 ):
            sum = sum + f( a + k * h )
            
        r[i,0] = (1 / 2) * r[i-1,0] + sum * h
        power4 = 1
        for j in range( 1, i + 1 ):
            power4 = 4 * power4
            r[i,j] = r[i,j-1] + ( r[i,j-1] - r[i-1,j-1] ) / ( power4 - 1 )
    ans  = r[i, j]
    return ans
