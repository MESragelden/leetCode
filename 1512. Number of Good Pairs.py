class Solution:
    def num_of_good_pairs(self, l: int) -> int:
        if l == 1 :
            return 1 
        else :
            return l + self.num_of_good_pairs(l-1)

    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dict = {}
        for ele in nums: 
            if ele in dict:
                dict[ele] += 1 
            else :
                dict[ele] = 1 
        for val in dict.values():
            if val >1:
                count += self.num_of_good_pairs(val-1)
        return (count)    
