x = input().split()
#x = [a for a in x if a >-1]
for i in x:
    if i < '0':
        x.remove(i)
print(x)