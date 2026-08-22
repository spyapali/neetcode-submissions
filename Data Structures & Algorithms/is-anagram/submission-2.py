class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        s_map = {} 
        t_map = {} 

        # populate the s_map 
        for char in s: 
            if char not in s_map: 
                s_map[char] = 1 
            else: 
                s_map[char] += 1 
        
        # populate the t_map 
        for char in t:
            if char not in t_map: 
                t_map[char] = 1 
            else:
                t_map[char] += 1 

        for char in s_map:
            if char not in t_map:
                return False 
            if s_map[char] != t_map[char]:
                return False 
        
        return True 

        