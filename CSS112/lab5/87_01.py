from cmath import sqrt
import math
n = int(input())
for i in range(3, n, 2):
    check = True
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            check = False
            break
    if check:
        print(i, end = ' ')
        