def findMaxLength(nums):
    count = 0
    d = dict()
    maxi = 0
    size = len(nums)
    s = []
    for i in range (0,size):
        if nums[i]== 1 :
            count += 1
        else :
            count -=1
        if (count == 0):
            maxi = i+1
        if(count in d ):
            maxi = max(maxi,i -d[count])
        else :
            d[count]= i 
    return maxi



k = [0,0,1,0,0,0,1,1]#6
j = [0,0,1,1,1,0] # 6
n = [0,1,0,0,1] # 4
m = [0,1]
u = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]
q = u[68:]
print("u = ", findMaxLength(u))

print("n = ", findMaxLength(n))
print("K = ", findMaxLength(k))
print("j = ", findMaxLength(j))

print("m = ", findMaxLength(m))

print(len(u))
