import numpy as np

m = np.array([[3, 2], [5, 6], [7, 1]])
#([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lst = [[] for i in range(len(m[0]))]
for i in range (len(m)):
    for j in range(len(m[i])):
        lst[j].append(m[i][j])
m = np.empty(len(m[0]))
for i in range(len(lst)):
    m[i] = int(max(lst[i]) - min(lst[i]))
print (m)