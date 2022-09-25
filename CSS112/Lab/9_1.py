x = []
x = input().split()
sum = 0
for i in range(5):
    sum += int(x[i - 1]) 
print(sum / 5)