"""# 1 ############################################################################################
def reverse(d):
    x = dict()
    for i in d:
        x[d[i]] = i
    return x

def keys(d, v):
    lst = list()
    for i in d:
        if d[i] == v:
            lst.append(i)
    return lst

exec(input().strip())
#print(reverse({3:"A", 2:"B"}) == {"A":3, "B":2})
#print(keys({3:33, 4:33, 5:55, 2:33}, 33))
#print(keys({3:33, 4:33, 5:55, 2:33}, 9999))
############################################################################################ 1 #
"""
"""
# 2 ############################################################################################
n = int(input())
d = dict()

for i in range(n):
    name, last_name = input().split()
    d[name] = last_name
    d[last_name] = name
n = int(input())

for i in range(n):
    q = input()
    if q in d:
        print(d[q])
    else:
        print("Not found")

10
Robert Dick
William Bill
James Jim
John Jack
Margaret Peggy
Edward Ed
Sarah Sally
Andrew Andy
Anthony Tony
Deborah Debbie
4
John
Jim
Don
Debbie
############################################################################################ 2 #
"""
"""
# 3 ############################################################################################
d = dict()
string = input()
for i in string:
    if not i.lower() in d:
        d[i.lower()] = 1
    else:
        d[i.lower()] += 1

lst = list()
for i in d:
    lst.append((-d[i], i))

x = sorted(lst)

for i in range(len(x)):
    a,b = x[i]
    print(b,"-->",-a)
############################################################################################ 3 #
"""

"""
# 10.1 ############################################################################################
n = int(input())
ans_u = set()
ans_in = set()
for i in range(n):
    lst = input().split()
    if i == 0:
        ans_in = set(lst).intersection(lst)
    else:
        ans_in = set(lst).intersection(ans_in)
    ans_u = set(lst).union(ans_u)

print(len(ans_u))
print(len(ans_in))
"""
"""
# 10.2 ############################################################################################
n = int(input())
win = list()
lose = list()
for i in range(n):
    winer,loser = input().split()
    win.append(winer)
    lose.append(loser)
print(set(win)-set(lose))
"""
"""
# 10.6 ############################################################################################
n = int(input())
d = dict()
for i in range(n):
    x,y = input().split(":")
    d[x] = y.split(",")

q = input()
ans = list()
for i in d:
    if i == q:
        continue
    #print(set(d[i]),(set(d[q])))
    if set(d[i]).intersection(set(d[q])) != set():
        ans.append(i)

if ans != []:
    print(ans)
else:
    print("Not Found")
"""


d = dict()
passed = dict()

x = input().split(" ")

lst = list()

while len(x) != 1:
    if x[0] not in d:
        d[x[0]] = (x[1],)
    else:
        d[x[0]] += (x[1],)
    if x[1] not in d:
        d[x[1]] = (x[0],)
    else:
        d[x[1]] += (x[0],)
    x = input().split(" ")

lst.append(x[0])
passed[x[0]] = 1

for i in d[x[0]]:
    if not i in passed:
        passed[i] = 1
        lst.append(i)
        
    for j in d[i]:
        if not j in passed:
            passed[j] = 1
            lst.append(j)
lst = sorted(lst)

print(lst)
