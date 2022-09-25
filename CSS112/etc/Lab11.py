#1
print("\n\n *** Lab week 11 - 1 *** ")

number = []
ans = []

Str = input("Input : ")                     #Input: str = 'ab138g579b'      Output: None
                                            #Input: str = 'h54325b1'        Output: 5
for i in Str:
    if i in number and not i in ans:
        ans.append(i)
    elif i >= '0' and i <= '9':
        number.append(i)
print("Output : ", end = ' ')
if len(ans) == 0:
    print(None)
    exit
ans.sort()
for i in ans:
    print(i, end = ' ')


#2
print("\n\n *** Lab week 11 - 2 *** ")

def check(Str = '\0'):
    if Str == '\0':
        return "Invalid parameter"
    ans = []
    number = []
    for i in Str:
        if i in number and not i in ans:
            ans.append(str(i))
        elif i <= '9' and i >= '0':
            number.append(i)
    if len(ans) == 0:
        return "None"
    ans.sort()
    answer = ' '.join(ans)
    return answer

print(check('ab138g579b'))  #Output: None
print(check('h54325b1'))    #Output: 5
print(check())              #Output: Invalid parameter
print("\n\n")