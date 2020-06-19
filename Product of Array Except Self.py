def productExceptSelf(nums):
    size = len(nums)
    product = 1
    zeros = 0
    for i in nums:
        if (i != 0):
            product *= i
        else :
            zeros +=1
    l = [] 
    if (zeros>1):
        for i in range (0,size):
            l.append(0)
    elif(zeros == 1):
        for i in range (0,size):
            if (nums[i]==0):
                l.append(product)
            else :
                l.append(0)
    else :
        for i in range (0,size):
            l.append(product//nums[i])
    return l


l = [0,1,9,0]
print(productExceptSelf(l))
        