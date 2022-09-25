"""temp = {'t1':10001010, 't2':100000010}

def sss(dc):
    for i in dc:
        ans = 0
        for j in range(1,len(str(dc[i]))):
            if(str(dc[i])[j] != str(dc[i])[j-1]):
                ans+=1
        dc[i] = ans
    return dc

temp = sss(temp)
print(temp)"""

a = [[1,[12,12]],[2,123123123],[3,[]]]
dt = {}
for i in a:
    if i[1] != []:
        dt[i[0]] = i[1]

print(dt)