import math
def reverse(x):
    if(x > 0):
        out = int(str(x)[::-1])
        if(out > 2**31 -1):
            return(0)
        return(out)
    else:
        out = int(str(x*-1)[::-1])
        if (out>(2**31 -1)):
            return(0)
        else :
            return (out*-1)
print(reverse(-123))