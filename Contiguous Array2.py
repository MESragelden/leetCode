def findMaxLength(nums):
    d = dict()
    longest = 0
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            sum -= 1
        else :
            sum += 1
        if sum == 0 :
            longest = i+1
        if sum in d:
            longest = max(longest,(i - d[sum]))

        else : 
            d[sum] = i
    return longest
    
print(findMaxLength([1,0,0,0,1,1]))