def search( nums,target):
        if nums is None or len(nums) == 0 or len(nums)==1 and nums[0] != target:
            return -1
        left,right = 0,len(nums)-1
        while left <=right:
            mid = (left + right)//2
            if(nums[mid] == target):
                return mid
            if target >=nums[0]:
                if (nums[mid]>=nums[0]  and target > nums[mid]):
                    left = mid + 1 
                else:
                    right = mid -1
            else :
                if (nums[mid]>=nums[0] or target >nums[mid]):
                    left = mid +1 
                else :
                    right = mid -1 
        return -1
nums = [15,14,13,12,11,10,9,8,7,6,0,1,2,3,4]
#nums = [0,1,8]
#nums = [4,5,6,7,0,1,2]
#target = 2
#nums = [4,5,6,7,8,1,2,3]
#nums= [3,5,1]
target = 99
print(search(nums,target))