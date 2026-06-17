class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = {}; // create map
        for(let s of strs) { 
            const count = new Array(26).fill(0);//array only 26 characters for alphabet
            for (let c of s ) {
                count[c.charCodeAt(0)- 'a'.charCodeAt(0)] += 1;// loop through words adding # of letters per word into the array 
            } 
            const key = count.join(',');//array to string 
            if (!res[key]) {//if the keys are new create a new group
                res[key] = [];//if not add it to group
            }
            res[key].push(s);  ////if not new add it to group
        }
        return Object.values(res); ////push all arrays formed into list
    }
}

