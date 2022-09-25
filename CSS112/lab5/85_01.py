x = input().split(",")
c = input()
d = list()
for i in x:
    sum = 0
    for j in i:
        if j == c:
            sum += 1
    d.append(sum)
print(d)
#d = [ e.count(c) for e in x]