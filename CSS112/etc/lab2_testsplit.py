#2
print(" *** lab week 10 - 2 *** ")
print()
def calc(str):
    print(str,"= ", end = '')
    lst = []    # 1023.5, 4, 17
    lstp = []   # +, -, /, *
    lstnum = []
    lst = str.split()
    for i in lst:
        if i in ('+', '-', '*', '/'):
            lstp.append(i) 
        else:
            lstnum.append(float(i))
    
    ans = lstnum[0]
    n = 1
    for i in lstp:
        if i == '+':
            ans += lstnum[n]
        elif i == '-':
            ans -= lstnum[n]
        elif i == '*':
            ans *= lstnum[n]
        elif i == '/':
            ans /= lstnum[n]
        n += 1
    
    print(ans)


calc("1023.5 + 4 - 17")
calc("12.34")
print()
print()

