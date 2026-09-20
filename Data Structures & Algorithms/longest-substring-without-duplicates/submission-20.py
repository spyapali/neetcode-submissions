

# i 
# bbbbb 

import sys 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} 
        start = 0
        max_count = 0 
        for end in range(len(s)):
            current_char = s[end]
            if current_char in seen: 
                start = max(start, seen[current_char] + 1)
            seen[current_char] = end 
            max_count = max(max_count, end - start + 1)
        return max_count




        