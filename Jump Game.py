class Solution:
    def canJump(self, nums):
        if nums is None or len(nums)==0:
            return False
        if len(nums)==1:
            return True
        size = len(nums)
        lastIndex=size-1
        for i in range (size-2,-1,-1):
            if i +nums[i] >= lastIndex:
                lastIndex = i
        print(lastIndex)
        return lastIndex == 0 
nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
s = Solution()
n = [3,2,1,0,4]
n2=[2,3,1,1,4]
print(s.canJump(nums))
        