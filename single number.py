#s import Set
def singlenum(A):
    s = set()
    for i in A :
        if i in s :
            s.remove(i)
        else:
            s.add(i)
    print(s.pop())



L1 =  [2,2,1]
L2 =  [4,1,2,1,2]
singlenum(L1)
singlenum(L2)