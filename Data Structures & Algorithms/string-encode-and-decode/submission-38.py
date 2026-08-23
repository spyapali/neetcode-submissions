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
        # print("final string: ", final_string)
        return final_string 

    def decode(self, s: str) -> List[str]:
        list_of_strings = []

        index = 0 

        #   i 
        # 2:we3:say1::3:yes10:!@#$%^&*() 
        # index 0 
        # len(s) - 1: 18 

        # "2" =>  50 (0)
        # ":"
        # charsToCount = 2 
        # index: 2 
        

        #       i 
        # 2:we3:say1::3:yes10:!@#$%^&*() 

        # index = 4 
        # newWord = "we" 
        # innerIndex: 2 
        # boundIndex: 3 
        # list_of_strings = ["we"]
        # index: 4 

        # curr_char = 3 
        # ord_current_char: 51 
        # chars_to_count = 3 
        # index: 6 


        #            i 
        # 2:we3:say1::3:yes10:!@#$%^&*() 

        # newWord = ""
        # innerIndex: 6 
        # boundIndex = 3 + 6 - 1 = 8 
        # newWord = "say"
        # list_of_strings = ["we", "say"]

        # current_char = "1" 
        # ord_current_char = 49 
        # charsToCount = 1 
        # index = 11 (9 + 2)

        # newWord = ":" 
        # innerIndex = 11 
        # boundIndex = 11  

        #                 i 
        # 2:we3:say1::3:yes10:!@#$%^&*() 

        # index = 12 

        # list_of_strings = ["we", "say, ":"]
        # current_char = "3"
        # ord_current_char = 51 
        # chars_to_count = 3
        # index = 14 
        # newWord = "" 
        # innerIndex = 14 
        # boundIndex = 3 + 14 - 1 = 16 

        # newWord = "yes"

        # list_of_strings = ["we", "say", ":", "yes"]


        #                              i 
        # 2:we3:say1::3:yes10:!@#$%^&*() 

        # index = 17 
        # current_char = 1
        # ord_current_char = 49 
        # counter = 17 
        # count = 1 
        # current_char = 10 
        # counter = 18 
        # count = 2 
        # index = 17 + 2  + 1 = 20 

        # chars_to_count = 10 
        # new_word = "" 
        # innerIndex = 20 
        # boundIndex = 10 + 20 - 1 = 29 

        # newWord = "!@#$%^&*()"
        # list_of_strings = ["we", "say", ":", "yes", "!@#$%^&*()"]
        # 20 + 10 = 30 
    
        #                   i 
        # 2:we3:say1::3:yes10:!@#$%^&*() 


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


