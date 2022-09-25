import math
r, theta = input().split()
x = math.cos(int(theta)) * int(r)
y = math.sin(int(theta)) * int(r)
print(x, y, end = ' ')