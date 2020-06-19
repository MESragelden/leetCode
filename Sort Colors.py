def sortColors(nums):        
        '''index = 0
        for i in range (len(nums)):
            if nums[i] == 0 : 
                nums[i],nums[index] = nums[index],nums[i] 
                index+=1
        index= len(nums ) -1
        for i in  reversed(range(len(nums))):
            if nums[i] == 2:
                nums[i],nums[index] = nums[index],nums[i]
                index -=1
        '''        
        zero_index = 0
        two_index = len(nums)-1
        equal = 0
        while (equal <= two_index):
            if nums[equal] == 0:
                nums[equal],nums[zero_index] = nums[zero_index],nums[equal]
                equal += 1
                zero_index +=1
            elif nums[equal] == 2 :
                nums[equal],nums[two_index] = nums[two_index],nums[equal]
                two_index -=1
            else :
                equal +=1
            
                
        print(nums)
sortColors([1,1,2,2,0,2,1,1,0,0,1])