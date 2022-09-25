import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = int(input())
for i in range (len(m)):
    for j in range(len(m[i])):
        if int(i + 1) % k == 0 and int(j + 1) % k == 0:
            m[i][j] = 0
print(m)