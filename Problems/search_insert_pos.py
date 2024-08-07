class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) # we will initilize the l and r here where l is 0 and r is the end of the array which is len(nums)
        while low<high:# as lond as l is less then right which it should be 
            mid = low + (high - low) // 2 # here we are computing where l + r the divide it by two like i wrttien before  
            # else r = mid -1 dont know why this is not a part of it but this is if the m is less the the target and we need to go toward the left 
            if target > nums[mid]: # so if the target id more the the mid then we ned to go up one 
                low = mid + 1
            else:
                high = mid # this if it they are = we will return that 
        return low # what if we dont find our target we will return our left pointer why left bc no matter which way we put the array the left will always be at the target