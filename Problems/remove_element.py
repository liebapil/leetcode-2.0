class Solution(object):
    def removeElement(self, nums, val):
    
        k = 0 # we are onl;t intializing the k here 

        for i in range(len(nums)): # here we will intrate through the length of nums
            if nums[i] != val: #if we see the i value then we dont want it then we will proform the swap so if its not val we will swap the num up
                 nums[k]= nums[i]# we can put it a positon k and tell us where to pur the next value  
                 k+=1 # then we will increment by 1 
        return k