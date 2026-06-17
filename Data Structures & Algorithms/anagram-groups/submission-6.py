class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       res = defaultdict(list)

       for s in strs: #count every string given in input
            count = [0]* 26 #a-z 26 values, one for each character

            for c in s : #every character in string
                count[ord(c) - ord ("a")] +=1 #ord for ascii, subtract ascii value of current charACTER MINUS a's ascii
            
            res[tuple(count)].append(s)

       return list (res.values()) 