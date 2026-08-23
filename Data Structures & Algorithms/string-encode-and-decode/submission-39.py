class Solution:

    # list of input words = ["hello", "tiger", "hallelujah", "peace", "love"]
    
    #  encoded string  
    #  i 
    # "5:hello5:tiger10:hallelujah5:peace4:love"
    
    # string="hello"

    # decoded string 
    # if it's a number, followed by a colon, start counting bytes. After counting bytes, should fall on another number. 
    # initialize a list 
    # loop through the string (while loop)
    #   for each char, check if it's within the ascii range for a number 
    #   if so store that in a var 
    #   ensure the value after that is a colon, and if it is, create an inner lop 
        # store those characters in a word 
    # add word to a list. 
    # increment the counter used for the loop  


    # strs = ["we","say",":","yes","!@#$%^&*()"]  

    #     i 
    # 2:we3:say1::3:yes10:!@#$%^&*() 

    # we

    # ["Hello","World"]
 
    def encode(self, strs: List[str]) -> str:
        final_string = "" 
        for s in strs: 
            final_string += str(len(s)) + ":" + s 
        return final_string 

    def decode(self, s: str) -> List[str]:
        list_of_strings = []

        index = 0

        while index < len(s) - 1:
            current_char = s[index]
            ord_current_char = ord(current_char)
            if 48 <= ord_current_char <= 57:
                if s[index + 1] == ":":
                    index += 2 
                else:
                    counter = index 
                    index_to_add = 1 
                    while s[counter + 1] != ":":
                        current_char += s[counter + 1] 
                        counter += 1 
                        index_to_add += 1  
                    index += index_to_add + 1

                chars_to_count = int(current_char)
                newWord = "" 
                inner_index = index 
                bound_index = chars_to_count + inner_index - 1 
                while inner_index <= bound_index and bound_index < len(s):
                    newWord += s[inner_index]
                    inner_index += 1 
                list_of_strings.append(newWord)
                index += chars_to_count 
    
        return list_of_strings 


