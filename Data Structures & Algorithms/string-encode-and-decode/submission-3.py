class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #encode , create new string
        for s in strs : #loop through all strungs
            res += str(len(s)) +"#" + s #new string is eual to length of the string + delimiter plus the actual string
        return res
    def decode(self, s: str) -> List[str]:
        res, i  = [], 0 #reference same string 

        while i < len(s) :
            j = i
            while s[j] != "#" :
                j+=1
            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res