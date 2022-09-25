# 1
n = int(input())
for i in range(n):
    for j in range(i * 2 + 1):
        print('*', sep='', end='')
    print('')

# 2
n = int(input())
for i in range(n):
    for j in range(n * 2 - i * 2 - 2) :
        print(' ', sep='', end='')
    for j in range(i * 2 + 1) :
        print('*', sep='', end='')
    print('')

# 3
n = 4
r = 10
print('Period       ',sep = '',end = '')
for i in range(1,r + 1):
    print(i,'%          ', sep = '', end = '')
print('')
for i in range(1,n + 1):
    print(i, '            ', sep = '', end = '')
    for j in range(1,r + 1):
        print('%.3f       '%(1 + (j / 100))**i, sep = '', end = '')
    print('')
