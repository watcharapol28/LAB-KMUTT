import math

x, y = input().split()
sum = z = complex(float(x), float(y));
sum = sum + z.conjugate()
if sum.real * 10 % 10 == 0:
    print(int(sum.real))
else:
    print(sum.real)