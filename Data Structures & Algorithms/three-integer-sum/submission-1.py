class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:#if i is same as its previous number it cant be separate a  , no duplicate triplets
                continue
            l, r = i+1, len(nums) - 1 #set pointers , 2 sum
            while l < r :
                threeSum = a + nums[l]  + nums[r] # add a + numbers from l,r pointer
                if threeSum > 0 :#if large 0 move r -1
                    r -= 1
                elif threeSum < 0 : #if less 0 move l + 1
                    l += 1
                else :
                    res.append([a,nums[l], nums[r]] ) #else add a to current nums on pointyers
                    l += 1
                    while nums[l] == nums[l-1] and l < r : #more than one solution so loop again, move l pointer +1when l same as previous 
                        l += 1
        return res