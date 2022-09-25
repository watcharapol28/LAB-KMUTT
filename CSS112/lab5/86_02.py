x = input().split()
x = [int(i) for i in x]
n = 0
for i in x:
    if i < 0:
        n += 1
print(n)
    