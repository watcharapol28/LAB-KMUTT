#1
print()
print(" *** lab week 10 - 1 *** ")
print()
def sum_is_even(s, t):
    while s < t: 
        num = s  
        check_even = 0
        while num != 0:
            check_even += num % 10
            num //= 10

        if check_even % 2 == 0:
            print(s, ",", sep = '', end = '')
        s += 1
    print()


sum_is_even(5, 20)
sum_is_even(95, 110)
sum_is_even(990, 1010)
print()
print()


#2
print(" *** lab week 10 - 2 *** ")
print()
def calc(str):
    print(str,"= ",end = '')
    str += ' '
    stack = []  # 1023.5
    lst = []    # 1023.5, 4, 17
    lstp = []   # +, -, /, *
    conti = False
    for i in str:
        #print(i)
        if conti:
            conti = False
            continue

        if i >= '0' and i <= '9' or i == '.' :
            #print("i=",i)
            stack.append(i)

        elif i == '-' or i == '+' or i == '*' or i == '/':
            #print("now",i)
            lstp.append(i)
            conti = True

        else:
            sum = 0
            n = 0
            for j in range(len(stack)-1, -1, -1):
                if stack[j] == '.':
                    sum /= 10**n
                    n = 0
                else:
                    sum += int(stack[j]) * 10**n
                    n += 1 
            lst.append(float(sum))
            stack = []
          
    #print(lst,lstp)
    ans = lst[0]
    j = 1
    for i in lstp:
        if i == '+':
            ans += lst[j]
        elif i == '-':
            ans -= lst[j]
        elif i == '*':
            ans *= lst[j]
        elif i == '/':
            ans /= lst[j]
        j += 1

    print(ans)


calc("1023.5 + 4 - 17")
calc("12.34")
print()
print()