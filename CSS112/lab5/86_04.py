x = input().split()
y = input().split()
z = [int(x[i]) + int(y[i]) for i in range(len(x))]
print(z)