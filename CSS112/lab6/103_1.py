n = int(input())
Dict = {}
ans = []
for i in range(n):
    x = input().split()
#    print(x)
    if not x[1] in Dict:
        Dict[x[1]] = (x[0],)
    else:
        Dict[x[1]] += (x[0], )
#    print(Dict)
fac = input().split()
for i in fac:
    for j in Dict[i]:
        if not j in ans:
            ans.append(j)
ans = sorted(ans)
for i in ans:
    print(i, end = ' ')
