x, y = input().split()

s = bin(int(x, 2) + (int(y, 2)))
ans = s[2:]

print(ans)