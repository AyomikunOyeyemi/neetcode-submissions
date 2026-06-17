class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = ""
        for (let s of strs){
            res += s.length + "#" + s;
        }
        return res;
    }
    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let i = 0;
        while(i < str.length){
            let k = i;
            while (str[k] !== "#"){
                k++;
            }
            let length = parseInt(str.substring(i, k));
            i = k + 1;
            k = i + length;
            res.push(str.substring(i, k));
            i = k;
        }
        return res;

    }
}
