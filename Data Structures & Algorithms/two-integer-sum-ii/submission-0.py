class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1 #create pointers

        while l < r : #codniton , pointers dont cross
            Sum = numbers[l] + numbers[r] #current sum

            if Sum > target : #if sum less than targ , move r pointer left(sorted array)
                r -= 1
            
            elif Sum < target : #vice verse, if first false then check thuis
                l += 1
            else : #if target = sum return this
                return [l+1, r+1]
