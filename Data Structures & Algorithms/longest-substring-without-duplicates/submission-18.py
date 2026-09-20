

import sys 

# 01234
# bbbbb
#  s
#   e 

# expand the window as long as all characters are non-repeating
# shrink the window when there's a repeating character 

#  {"b": 1}
#  count = end - start + 1 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0 
        seen = {} 
        start = 0 
        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]] + 1)
            seen[s[end]] = end 
            max_count = max(max_count, end - start + 1)
        return max_count




        