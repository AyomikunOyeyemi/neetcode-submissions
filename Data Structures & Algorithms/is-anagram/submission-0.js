class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length){
            return false;
        }
    
    const counting = new Array(26).fill(0);
    for (let i =0 ; i < s.length ; i++) {

    counting[s.charCodeAt(i) - 'a'.charCodeAt(0)] ++;
    counting[t.charCodeAt(i) - 'a'.charCodeAt(0)] --;
    }
return counting.every((val) => val === 0);
    }
}