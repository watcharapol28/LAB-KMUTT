n = int(input())
c = []
c = [[j for j in range(i*2, n, i)]for i in range(2, n)]

lst =[]
for i in c:
    for j in i:
        lst.append(j) 
lst.sort()

ans = []
for i in range(len(lst) - 1):
    if not lst[i] == lst[i + 1]:
        ans.append(lst[i])
ans.append(lst[len(lst) - 1])

print(ans)