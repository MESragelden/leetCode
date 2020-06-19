def subarraySum(nums, k):
    if nums is None or len(nums) == 0:
        return 0
    count = 0
    last = 0
    d = dict({0:1})
    for i in range (0,len(nums)):
        last +=  nums[i]
        if (last - k) in d:
            count +=d[last - k]
        if(last in d):
            d[last] +=1
        else :
            d[last] = 1
    for k,v in d.items():
        print (k,"*"*8,v)
    return count
nums = [3,4,7,2,-3,1,4,2]
k = 7
num1 = [-1,-1,1]

k1 = 0
print(subarraySum(num1,k1) )



