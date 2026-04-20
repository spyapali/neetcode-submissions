
# 
# bab

# gag

#    e 
# s 
# noon 

# 
# mom 
# ybaby

class Solution:
    def isPalindrome(self, s: str) -> bool:
        startPtr = 0 
        endPtr = len(s) - 1 
        while startPtr <= endPtr:
            if s[startPtr].lower() == s[endPtr].lower():
                startPtr += 1
                endPtr -= 1 
            elif s[startPtr].isalnum() == False: 
                startPtr += 1 
            elif s[endPtr].isalnum() == False: 
                endPtr -= 1 
            else: 
                return False 

        return True 


        