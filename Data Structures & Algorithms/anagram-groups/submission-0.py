class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for i in range(len(strs)):
            current_word = strs[i]
            sorted_current_word = "".join(sorted(current_word))
            if sorted_current_word in sorted_words: 
                sorted_words[sorted_current_word].append(current_word)
            else: 
                sorted_words[sorted_current_word] = [current_word]
        return [value for value in sorted_words.values()]

                

        
        # ["act","pots","tops","cat","stop","hat"]
