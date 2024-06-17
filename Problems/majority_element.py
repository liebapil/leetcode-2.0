class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} # lets creste a hashmap 
        res, maxCount = 0,0 # keep track of the max valur and set it to 0 its just the candiate we dont know yet

        for n in nums: # for each value
            count[n]= 1+count.get(n,0) # each vaue we want to igrament it by 1 and if not then we cna send result to 0 
            res = n if count[n] > maxCount else res # if its greater then the max count we update and if not we can keep the result 
            maxCount =max(count[n], maxCount) # we should keep the max count so the n and the max count it is 
        return res # we retrun the results 
