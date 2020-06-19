def rangeBitwiseAnd(m,n):
    
    def sameNumOfBits(st,end):
        count = 0
        while(st >=0 or end >=0):
            if(st == end):
                return True,count,st
            if (st == 0 and end == 0):
                return True,count,0
            elif (st >0 and end == 0):
                return False,count,1
            elif (end > 0 and st ==0):
                return False,count,1
            else :
                count +=1
                st >>=1
                end >>= 1
    if n == m :
        return n
    condition ,onesPlace,st = sameNumOfBits(m,n)
    if(not condition):
        return 0
    else :
        #print (onesPlace)
        result =st<<onesPlace
        start = 1<<onesPlace-1
        while(start >0):
            if(start & m  !=0):
                result |=start
                start = start>>1
            else :
                break 
    return result
    
print(rangeBitwiseAnd(10,11))
# 10,11
# 223,240
# 5,7        