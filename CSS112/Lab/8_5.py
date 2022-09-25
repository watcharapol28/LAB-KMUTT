import math
x, y = input().split()
r = math.sqrt(int(x)**2 + int(y)**2)
theta = math.atan(y / x)
print(r, theta, end = ' ')