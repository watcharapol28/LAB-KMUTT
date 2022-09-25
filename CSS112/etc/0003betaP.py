m, n = input().split()
m, n = int(m), int(n)
mtrix1, mtrix2 = [], []
for i in range(m):
    mtrix1.append(input().split())
    #print(i,"M1 ",mtrix1, sep = '')
for i in range(m):
    mtrix2.append(input().split())
    #print(i,"M2 ",mtrix2, sep = '')
for i in range(m):
    for j in range(n):
        print(int(mtrix1[i][j]) + int(mtrix2[i][j]), end = ' ')
    print()