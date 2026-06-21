class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #create a hashmap/dictionary

        for i, n in enumerate(nums) : #loop thru nums looking at index  and value
            diff = target - n  #diff is the complement,do target - value  
            if diff in prevMap : # check if the complement is alr in hash
                return [prevMap[diff], i] #return the diff number where we first saw it  and the current index
            prevMap[n] = i 
        