def ranges(end, start = 0, step = 1):
    print("(", float(start),", ", end = '', sep = '')

    while(1):
        start += step
        if(start + step >= end):
            print(round(float(start), 3), ")", end = '', sep = '')
            break
        print(round(float(start), 3), end = ', ')

print("*** New Range ***")
x = input("Enter Input : ")
num = x.split()
if len(num) == 1:
    ranges(float(num[0]))
elif(len(num) == 2):
    ranges(float(num[1]), float(num[0]))
else:
    ranges(float(num[1]), float(num[0]), float(num[2]))