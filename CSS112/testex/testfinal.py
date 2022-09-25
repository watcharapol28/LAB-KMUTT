class Object1:
    def __init__(self,a):
        self.a = a[0]
        self.b = a[1]
        
    def __str__(self):
        return f"Object1({self.a},{self.b})"
        
    def __gt__(self,other):
        return sorted(self)#Your Code Here

a = [(2,3),(9,5),(4,-2),(0,8)]
aObj1s = [Object1(i) for i in a]
for i in aObj1s:
    print(i)

aObj1sSorted = sorted(aObj1s)#Your Code Here
print(aObj1sSorted)