/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    for(let r = 0; r<nums.length; r++ ){ ///iterate through the length of the array 
        for (let l=0; l<r; l++){ //// make sute left is smaller the right 
            const dup=nums[l]===nums[r] ///if they are == then return true
            if (dup)
            return true 
        }
    }
    return false /// if not false 
};