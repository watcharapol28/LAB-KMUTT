lst = []
for i in range(6):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if (x,y) not in lst:
        lst.append((x,y))
        
print(lst)
