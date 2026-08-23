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
            # print("ord_current_char: ", ord_current_char)
            # check if char is between "0" to "9"
            if 48 <= ord_current_char <= 57:
                # print("current index: ", index)
                if s[index + 1] == ":":
                    index += 2 
                    # print("charsToCount: ", charsToCount)
                    # skip the current number and the colon
                else:
                    counter = index 
                    count = 1 
                    chars_to_add = ""
                    while s[counter + 1] != ":":
                        chars_to_add += s[counter + 1] 
                        counter += 1 
                        count += 1  
                    index += count + 1
                    current_char += chars_to_add

                charsToCount = int(current_char)
                # print("charsToCount: ", charsToCount)
                # print("index after increment: ", index)
                # if index >= len(s):
                #     break
                # start the inner loop of counting, and initialize word
                newWord = "" 
                innerIndex = index 
                # print("innerIndex: ", innerIndex)
                boundIndex = charsToCount + innerIndex - 1 
                # print("boundIndex: ", boundIndex)
                # print("I'm getting here")
                while innerIndex <= boundIndex and boundIndex < len(s):
                    newWord += s[innerIndex]
                    innerIndex += 1 
                list_of_strings.append(newWord)
                # print("list_of_strings: ", list_of_strings)
                index += charsToCount 
                # print("index after counting: ", index)
                # print("index after charsToCount: ", index + charsToCount)
    
        return list_of_strings 


