"""# 1
n = int(input())
for i in range(n):
    print('*'*(i * 2 + 1), sep='')"""

# 2
n = int(input())
for i in range(n):
    print(' '*(n * 2 - i * 2 - 2), '*'*(i * 2 + 1), sep='')