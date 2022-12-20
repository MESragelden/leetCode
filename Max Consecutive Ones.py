class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #print(len(nums))
        maximum = 0 
        current = 0 
        for ele in nums:
            if ele == 1 :
                current +=1              
            else:
                print (current)
                if maximum < current :
                    maximum = current 
                current = 0
        return max(maximum,current)
        
        