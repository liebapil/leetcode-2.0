var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        for (let j = (i + 1); j < nums.length; j++) {
            const num = nums[j];

            const isTarget = num === complement
            if (isTarget) return [ i, j ];
        }
    }

    return [ -1, -1 ];
};