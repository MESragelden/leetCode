class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array = []
        total = 0
        for elem in nums:
            total += elem
            sum_array.append(total)
        return sum_array