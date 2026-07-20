class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        while l < r :
            while l < r and not self.alphaNum(s[l]):  #use self as alphanum is another function in the class solution class, so checks in its self
                l += 1  #make sure l is alphaNum, if not increment
            while r > l and not self.alphaNum(s[r]): #make sure alphaNum , r>l constraints so pointers dont break boundaries
                r -= 1
            if s[l].lower() != s[r].lower(): #if the pointers arent the same return false, .lower for Lcase
                return False
            l,r = l + 1, r -1  #this to move to next string for both pointerd 
        return True


    
    def alphaNum(self, c) : #create alphanum function
        return (ord ('A') <= ord(c) <= ord('Z') or # if c is between ascii of A-Z then valid
                ord ('a') <= ord(c) <= ord('z') or # if c is between ascii of a-z then valid
                ord ('0') <= ord(c) <= ord('9'))    # if c is between ascii of 0-9 then valid