number = {}
x = input()
for i in range(len(x)):
    if x[i] >= '0' and x[i] <= '9':
        number[int(x[i])] = True

ans = []
for i in range(10):
    if not i in number:
        ans.append(i)

if len(ans) == 0:
    print("None")
else:
    print(*ans, sep = ',', end = '')