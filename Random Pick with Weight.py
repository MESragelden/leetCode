class Solution:
    
    def __init__(self, w):
        from itertools import repeat 
        self.prefix_sum = []
        pre = 0
        for wei in w :
            pre += wei
            self.prefix_sum.append(pre)
        self.total = pre
        print(self.prefix_sum)

    def pickIndex(self) -> int:
        import random
        input = random.random()*self.total
        low,high = 0,len(self.prefix_sum)
        while(low <high):
            mid = low +(high-low)//2
            if input > self.prefix_sum[mid]:
                low = mid +1
            else :
                high = mid
        return low

        


# Your Solution object will be instantiated and called as such:
w = [1,3]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)