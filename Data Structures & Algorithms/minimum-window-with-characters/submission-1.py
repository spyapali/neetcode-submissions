class Solution:

    # Input: s = "OUZODYXAZV", t = "XYZ"
    # Output: "YXAZ"

    # original = {"X": 1, "Y": 1, "Z": 1}

    #          e 
    #      s 
    # OUZODYXAZV
    # 0123456789

    # need = {}
    # maxLength = 4 
    # new_string = "YXAZ"

    from collections import Counter 

    def minWindow(self, s: str, t: str) -> str:
        min_length = len(s) + 1
        result = [None, None]
        count = Counter(t)
        need = len(count)
        have = 0
        current = {} 
        start = 0 


        for end in range(len(s)):
            current_char = s[end]
            if s[end] in count: 
                current[s[end]] = current.get(s[end], 0) + 1
                if current[s[end]] == count[s[end]]:
                    have += 1 
            while have == need:           
                if (end - start + 1) < min_length:
                    min_length = end - start + 1 
                    result = [start, end]
                if s[start] in count:
                    current[s[start]] -= 1
                    if current[s[start]] < count[s[start]]:
                        have -= 1  
                start += 1 
        
        if result[0] == None and result[1] == None:
            return ""
        return s[result[0]:result[1] + 1]



        
        
        









        