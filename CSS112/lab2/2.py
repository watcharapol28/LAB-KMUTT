x = input()
y = input()
x = x.split()
nub = 1
for i in x:
    if i == y:
        print(nub, end = '')
        nub += 1
    else:
        print(i, end = '')
    print(" ", end = '')

