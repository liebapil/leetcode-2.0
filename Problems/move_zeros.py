class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0 # the l is in the begining 
        for r in range(len(nums)): # the r will be in the begiming but it will itrate throught the entrie array 
            if nums[r]: # if the r is 0 leave it but if the nums not 0 then
                nums[l], nums[r] = nums[r], nums[l]# we swap the l index with the r index which in python its done easily and can be done with this simple algrithim 
                l +=1 # then move the l and icreament bc the r will already moce with the range one 
        return nums # then return the array 