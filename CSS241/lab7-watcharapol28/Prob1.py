import numpy as np

def GaussianForwardElimination(A,b): #A,b are numpy array of size (n,n) and n for equation Ax=b
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    Aans = A.copy()
    bans = b.copy()

    for now in range(bn - 1):
        for i in range(now + 1, m):
            vQ = Aans[i][now] / Aans[now][now]
            # print(vQ)
            for j in range(now, n):
                Aans[i][j] -= vQ * Aans[now][j]
                # print("A[",i,j,"]",Aans[i][j])
            bans[i] -= vQ * bans[now]
        print(Aans, bans)

    return Aans,bans


def GaussianBacksubstitution(A,b):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    x = np.zeros(n,dtype=np.float64)
    print("x",x)
    for now in range(bn - 1, -1, -1):
        sum = 0
        # print("Bnow [",now, "] = ", b[now])
        print("Xnow ",x[now])
        for j in range(n - 1, now, -1):
            print("XJ = ",x[j])
            sum += A[now][j] * x[j]
        # print("sum",sum)
        x[now] = (b[now] - sum) / A[now][now]
                
    return x

def Problem1(A,b): 
    Aelem, belem = GaussianForwardElimination(A,b)
    x = GaussianBacksubstitution(Aelem,belem)
    return x

x=[[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
y=[16,26,-19,-34]
xx = np.array(x,dtype=np.float64)
yy = np.array(y, dtype=np.float64)

print(Problem1(xx,yy))