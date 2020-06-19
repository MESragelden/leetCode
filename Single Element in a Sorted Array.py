def singleNonDuplicate(nums):
    lenght = len(nums)
    if lenght == 1 :
        return nums[0]
    start = 0
    end = lenght -1 
    while (end > start):
        middle = (start + end )//2
        if middle %2 == 0:
            if nums[middle] != nums[middle +1]:
                end = middle
            else :
                start = middle +1
        else : 
            if nums[middle] == nums[middle -1]:
                start = middle+1 
            else :
                end = middle 
    return nums[start]
        
print(singleNonDuplicate([3,3,7,7,10,11,11]))
# [1,1,2,3,3,4,4,8,8]
# [3,3,7,7,10,11,11]