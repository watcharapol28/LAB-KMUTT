import numpy as np

k = int(input())
c = np.array([[(i+j)%2 for j in range(k)]for i in range(k)])
print(c)