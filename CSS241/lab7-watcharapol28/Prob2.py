#64090500421
import numpy as np

def GaussianSwapForwardElimination(A,b):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    Aans = A.copy()
    bans = b.copy()
    l = list(range(n))
    sl = np.abs(A).max(axis=1)

    # print(Aans,bans,l)
    xx =[]
    for p in range(len(l)):
        Max = -100
        for i in range(p, len(l)):
            if l[i] not in xx:
                value = abs(Aans[l[i]][l[p]] / sl[l[i]])
                if Max < value:
                    Max = value
                    point = i
        s = l[point]
        l[point] = l[p]
        l[p] = s
        xx.append(s)
        
        for now in range(p, len(l)):
            if now == l[p] :
                continue
            vQ = Aans[now][p] / Aans[l[p]][p]
            for i in range(p, m):
                Aans[now][i] -= vQ * Aans[l[p]][i]
            bans[now] -= vQ * bans[l[p]]
        # print(Aans,bans,l)

    
    return Aans,bans,l

def GaussianSwapBacksubstitution(A,b,l):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    x = np.zeros(n,dtype=np.float64)
    #Your Code Here
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(n-1,i,-1):
            # print(A[l[i],j], x[l[i]])
            sum += A[l[i]][j] * x[l[j]]
        # print("xli",x[l[i]], "sum =",sum )
        # print("Ali ",A[i][i])
        # print("sum=",(b[l[i]]-sum)/A[l[i]][l[i]])
        x[l[i]] = (b[l[i]] - sum) / A[l[i]][i]
        # print(x[l[i]])
    
    ans = np.zeros(n,dtype=np.float64)
    for i in range(len(l)):
        # print(i,x[i])
        ans[i]=x[l[i]]

    # print(ans)     
    # End your code
    return ans

def Problem2(A,b):
    Aselem,bselem,l = GaussianSwapForwardElimination(A,b)
    # print(Aselem,bselem,l)
    x = GaussianSwapBacksubstitution(Aselem,bselem,l)
    return x

# x = [[3,-13,9,3],[-6,4,1,-18],[6,-2,2,4],[12,-8,6,10]]
# y = [-19,-34,16,26]
# xx = np.array(x,dtype=np.float64)
# yy = np.array(y, dtype=np.float64)
# print(Problem2(xx,yy))
