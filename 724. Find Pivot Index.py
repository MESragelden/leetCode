class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = sum(nums)
        i = 0
        while (i<length):
            right -= nums[i]
            if(right == left):
                return i 
            else :
                print("left == {}, right == {}, nums[i] == {}".format(left,right,nums[i]))
                left += nums[i]
                i +=1 
        return -1 
