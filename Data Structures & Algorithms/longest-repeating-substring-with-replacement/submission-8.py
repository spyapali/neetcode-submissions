
class Solution:

#    e 
# s 
# ABBB
# 2
# {"A": 1, "B": 3}
# maxF = 3 
    # k = 2 
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {} 
        max_count = 0 
        maxf = 0 
        start = 0 
    
        for end in range(len(s)):
            frequencies[s[end]] = frequencies.get(s[end], 0) + 1 
            maxf = max(maxf, frequencies[s[end]])

            # if the window is too big 
            if (end - start + 1) - maxf > k: 
                # shrinking the window 
                frequencies[s[start]] -= 1 
                start += 1

        return end - start + 1

    # max_count = 2 

    # next_start_index = 1 
    # replacements = 0
    # start = 4 
    # end = 4 




        
        