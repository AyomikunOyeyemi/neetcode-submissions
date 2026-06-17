class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const twoNums = new Map();
        for (let i = 0; i< nums.length ;  i++){
            const complement = target - nums[i];
        
        if (twoNums.has(complement)) {
            return [twoNums.get(complement), i];
        }
        twoNums.set(nums[i], i);
    }
    return [];
    }
}
