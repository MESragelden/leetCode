class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos_inx = 0
        neg_inx = 0
        output = []
        size = len(nums)
        first = nums[0]
        last = nums[size-1]
        # if nums are all positive 
        if (first >=0) and (last > 0):
            return  [i ** 2 for i in nums]
        # nums are negative
        elif (first <0) and (last <=0):
            for i in reversed(nums):
                output.append(i*i)
            return output
        # Normal Case positive and negative
        else :
            i = 0
            while i < len(nums):
                if nums[i]< 0:
                    i +=1 
                else:
                    pos_inx = i 
                    neg_inx = i -1 
                    break
        
            while (pos_inx < size) and (neg_inx > -1) :
                print("Positive index {},  Negative index {}, size = {}".format(pos_inx,neg_inx,size))
                if nums[pos_inx] <= abs(nums[neg_inx]) :
                    output.append(nums[pos_inx] * nums[pos_inx])
                    pos_inx += 1
                else:
                    output.append(nums[neg_inx] * nums[neg_inx])
                    neg_inx -= 1
            if (pos_inx == size and neg_inx == -1):
                return output
            elif neg_inx == -1 :
                for i in range (pos_inx,size):
                    output.append(pow(nums[i],2))
              
            #if pos_inx == size:
            else:
                i = neg_inx
                while i > -1:
                    output.append(pow(nums[i],2))
                    i -= 1
                
            
            return output 