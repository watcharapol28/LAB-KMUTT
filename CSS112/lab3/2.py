nub = 0
sum = 0
while True:
    x = input()
    if x == "q":
        break
    sum += float(x)
    nub += 1
if nub == 0:
    print("No Data")
else:
    ans = float("{:.2f}".format(sum/nub))
    print(ans) 
