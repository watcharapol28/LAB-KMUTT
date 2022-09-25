x = input().split()
x = [int(i) for i in x]
lst = []
x.sort()
for i in range(len(x) - 1):
    if not x[i] == x[i + 1]:
        lst.append(x[i])
lst.append(x[len(x) - 1])
print(lst)