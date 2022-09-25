print(" *** Lab week 12 - 1 *** ")

def mypi(n):
    sum = 3
    now = 2
    for i in range(n):
        sum_insq = 1
        for j in range(3):
            sum_insq *= now
            now += 1
            #print(now)
        now -= 1
        if i % 2 == 0:
            sum += 4/sum_insq
        else:
            sum -= 4/sum_insq
    return sum


for i in range(30):
    print(' %2d' %(i + 1), mypi(i + 1), sep = '   ')



print("\n\n *** Lab week 12 - 2 *** ")

from random import randint

list_num = []

while len(list_num) < 10:
    num = randint(0, 9)
    if not num in list_num:
        list_num.append(num)

str_num = [str(int) for int in list_num]
plist = ','.join(str_num)
print(plist)
num_ip = 10

while True:
    num_ip = int(input("> "))
    if not num_ip in list_num:
        break
    list_num.remove(num_ip)
    list_num.insert(0, num_ip)
    str_num = [str(int) for int in list_num]
    plist = ','.join(str_num)
    print(plist)
#    shuffle

print(" -- End your program -- ")


