class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const twoMap = new Map ();
        for(let i = 0; i < nums.length; i++) {
            const complement = target - nums[i];
        
        if(twoMap.has(complement)) {
            return [twoMap.get(complement),i];
        }
        twoMap.set(nums[i], i);
     }
    
     return [];
 }
}