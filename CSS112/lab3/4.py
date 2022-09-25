x = input()
y = input()
if len(x) != len(y):
    print("Incomplete answer")
else:
    sum = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            sum += 1
    print(sum)