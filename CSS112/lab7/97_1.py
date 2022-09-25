p_icecream = {}

n = int(input())

for i in range(n):
    name, price = input().split()
    p_icecream[name] = price

n = int(input())

sale = {}

sum = 0

for i in range(n):
    name, value = input().split()
    if name in p_icecream:
        sum += int(value) * int(p_icecream[name])
        if name in sale:
            sale[name] += int(value) * int(p_icecream[name])  
        else:
            sale[name] = int(value) * int(p_icecream[name])


if len(sale) == 0:
    print("No ice cream sales")

else:
    ans = []
    mn = -1
    for i in sale:
        if mn < sale[i]:
            mn = sale[i]
            ans = []
            ans.append(i)
        elif mn == sale[i]:
            ans.append(i)
    ans = sorted(ans)
    print("Total ice cream sales:", sum)
    print("Top sales: ", end = '')
    for i in range(len(ans) - 1):
        print(ans[i], end = ', ')
    print(ans[len(ans) - 1])
    #Total ice cream sales: 1020.0
    #Top sales: Cornetto, Magnum
