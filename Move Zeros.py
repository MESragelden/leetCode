
def moveZeros(L):
    size = len(L)
    for i in range (0,size):
        if(L[i]==0):
            for j in range (i+1,size):
                if(L[j] != 0):
                    L[i],L[j] = L[j],L[i]
                    break
    print(L)



'''
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
L = [0,1,0,3,12]
moveZeros(L)