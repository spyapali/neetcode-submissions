# Input: strs = ["act","pots","tops","cat","stop","hat"]

# dict = {"act": ["act"], "opst": ["pots", "tops", "stop"], "aht": ["hat"]]}


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagrams: 
                anagrams[sorted_s].append(s)
            else: 
                anagrams[sorted_s] = [s]

        return [anagrams[key] for key in anagrams]
        