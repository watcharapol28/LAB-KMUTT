passage = input()
#Being with you I reign in university, the sporty look of mine energize my list. I am going outing in university email
num = list(input().split(','))
#0,12,5,4,1,1,1,1,1,6,4,1,1,1,1,1,1,1,4,1,6,1,1,6,1,1,7,1,1,2,1,3,3,1,8,1,3,1,1,4,6

test = []
sum = 0
for i in num:
    sum += int(i)
    test.append(passage[sum])

for i in test:
    print(i, end = '')