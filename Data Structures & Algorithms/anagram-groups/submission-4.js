class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const result = {};
        for(let s of strs){
            const count = new Array(26).fill(0);
            for(let c of s ){
                count[c.charCodeAt(0)- 'a'.charCodeAt(0)] +=1;
            }
            const key = count.join(",");//array to string
            if(!result[key]){//if key not exist , new bucket
                result[key] = [];
            }
            result[key].push(s);
        }
    return Object.values(result);
    }
}
