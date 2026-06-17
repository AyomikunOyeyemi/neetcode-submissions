class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {};
        const freq = Array.from({length: nums.length + 1} , () => []);
        for  (const n of nums){
            count[n] = (count[n] || 0) +1;
        }
        for (const n in count) {
            freq[count[n]].push(parseInt(n));
        }
        const results = [];
        for(let i = freq.length - 1; i > 0; i--){
            for(const n of freq[i]){
                results.push(n);
                if (results.length === k){
                    return results;
                }
            }
        }
    }
}
