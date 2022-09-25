d = dict()
string = input()
for i in string:
    if not i.lower() in d:
        d[i.lower()] = 1
    else:
        d[i.lower()] += 1
sort_d = sorted(d)
lst = list()
for i in sort_d:
    lst.append((-d[i], i))

x = sorted(lst)

for i in range(len(x)):
    a,b = x[i]
    print(b,"-->",-a)