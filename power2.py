import math 
def isPowerOfTwo(n):
    out = n & (n-1)
    if(out == 0):
        return True
    return False
print(isPowerOfTwo(536870912))