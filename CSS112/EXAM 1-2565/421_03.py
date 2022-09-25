ftpassage = input()
#Being with you I reign in university, the sporty look of mine energize my list. I am going outing in university email
scpassage = input()
#Born in us, the spy of enemy is amoung us
sum = 0
now = 0
ans = []
for i in scpassage:
    while i != ftpassage[int(sum)]:
        sum += 1
    ans.append(int(sum - now))
    now = sum
print(ans)
