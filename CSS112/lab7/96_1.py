myd = {}
x = input()

for i in range(len(x)):
    if x[i] in myd:
        myd[x[i]] = myd[x[i]] + 1
        continue
    myd[x[i]] = 1

d2 = {}

for i in myd:
    if myd[i] in d2:
        d2[myd[i]] += (i,)
        continue
    d2[myd[i]] = (i,)

lst_count = [i for i in d2]
lst_count = sorted(lst_count, reverse = True)

for i in lst_count:
    sort_d2i = sorted(d2[i])
    for j in sort_d2i:
        print(j, "->", i)

