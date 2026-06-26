class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #new dictionary/hashmap
        fre = [[]  for i in range(len(nums) +1 )]  #our new array same size as input array

        for n in nums : 
            count[n] = 1 + count.get(n, 0)
        
        for n,c in count.items(): #returns ever key value pair
            fre[c].append(n)

        res = []
        for i in range(len(fre)- 1, 0, -1): #-1last index, go all the way to 0 , since negative -1 as decrementer
            for n in fre[i]:
                res.append(n)
                if len(res) == k:
                    return res