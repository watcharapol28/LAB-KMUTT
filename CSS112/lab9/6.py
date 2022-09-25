import numpy as np

k = int(input())
c = np.array([[i+1 if(i+j)%2==0 else 0 for j in range(k)]for i in range(k)])
print(c)