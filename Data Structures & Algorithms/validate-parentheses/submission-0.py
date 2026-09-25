#   i 
# ["(", ")", "{", "}", "[", "]"]

#  i 
# ([{}]))
# stack = ["("]

# ")"

# utilize a while loop 
#   
#   c 
# ["(", ")", "{", "}", "[", "]"]
class Solution:
    def isValid(self, s: str) -> bool:
        chars = set(["(", "{", "["])
        stack = [] 
        open_chars = {
            ")": "(", 
            "}": "{",
            "]": "["
        }
        pointer = 0 
        while pointer < len(s): 
            char = s[pointer]
            if char in chars:
                stack.append(char)
            else:
                if stack == []: 
                    return False 
                open_char = stack.pop()
                if open_chars[char] != open_char: 
                    return False
            pointer += 1 
        if len(stack) > 0:
            return False 
        
        return True 


            


            

            



            

        


        