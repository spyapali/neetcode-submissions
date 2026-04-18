class Solution:

    DELIMITER = '\u0100'  # outside 0-255, safe from collisions ✅


    def encode(self, strs: List[str]) -> str:
        # encoded_str: "sally" ==> "ucmm{"
        # decoded_str: "sally"
        if strs == []: 
            return "\u2605"
        encoded_words = [] 
        for word in strs: 
            new_word = "" 
            for char in word: 
                ascii_char = ((ord(char) + 2) % 256)
                new_char = chr(ascii_char)
                new_word += new_char 
            encoded_words.append(new_word)
        combined_string = self.DELIMITER.join(encoded_words)
        print(combined_string)
        return combined_string

    def decode(self, s: str) -> List[str]:
        if s == "\u2605":
            return []
        encoded_words = s.split(self.DELIMITER)
        decoded_words = [] 
        for word in encoded_words:
            new_word = ""
            for char in word:
                ascii_char = ((ord(char) - 2) % 256)
                new_char = chr(ascii_char)
                new_word += new_char  
            decoded_words.append(new_word)
        return decoded_words
            
