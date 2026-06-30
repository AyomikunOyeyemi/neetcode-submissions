class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fre = [[] for i in range(len(nums) + 1)] 

        for n in nums :
            count[n] = count.get(n,0) + 1
        
        for n,c in count.items() :
            fre[c].append(n)

        res = []
        for i in range(len(fre)-1,0,-1) :
            for n in fre[i]:
                res.append(n)
                if len(res) == k :
                    return res