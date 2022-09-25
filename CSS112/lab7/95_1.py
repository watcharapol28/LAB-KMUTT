n = int(input())
d = {}

for i in range(n):
    name, nickname = input().split()
    d[name] = nickname
    d[nickname] = name

n = int(input())
lst = []

for i in range(n):
    check = input()
    if check in d:
        lst.append(d[check])
        continue
    lst.append("Not found")

for i in lst:
    print(i)