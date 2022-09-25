x = input()
y = input()
y = y.split()
sum = 0


for i in y:
    s = ''.join(ch for ch in i if ch.isalnum())
    if s == x:
        sum += 1

print(sum)