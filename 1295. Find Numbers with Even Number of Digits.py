class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for elem in nums:
            if (len(str(elem))%2 ==0):
                sum +=1
        return sum