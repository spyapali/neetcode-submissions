class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracker = {}
        result = 0

        for i in range(len(nums)):
            num = nums[i]
            if num - 1 in tracker:
                tracker[num] = tracker[num - 1] + 1
            else:
                tracker[num] = 1
            while num + 1 in tracker:
                tracker[num + 1] = tracker[num] + 1
                num+=1
            result = max(result, tracker[num])
        
        # print(tracker)
        return result

# class Solution:

    
#     #  nums         
#     #  i 
#     # [2,20,4,10,3,4,5]

#     # longestConsecutiveSequence = 2 
    
#     #                
#     #       i  
#     # [2,20,4,10,3,4,5]
#     # [{2:1}, {20:1}, {4:1}, 1, 1, 1]

#     # consecutiveSequence 
#     # {2: 1, 20: 1, 4: 1, 10: 1, 3: 2, 4: 3, 5: 4}
#     # smallestNum = 2 

#     #              i  
#     # [0,3,2,5,4,6,1,1] 
#     # longestSequence: 
    

#     # consecutiveSequence 
#     # {0: 1, 3: 4, 2: 3, 5: 6, 4: 5, 6: 7, 1: 2, 1: 2}


#     def longestConsecutive(self, nums: List[int]) -> int:
#         longest_consecutive_sequence = 0

#         sequence = {} 
#         for num in nums: 
#             if num - 1 in sequence:
#                 sequence[num] = sequence[num - 1] + 1 
#             else:
#                 sequence[num] = 1
#             while num + 1 in sequence:
#                 sequence[num + 1] = 1 + sequence[num]
#                 num = num + 1 
#             longest_consecutive_sequence = max(sequence[num], longest_consecutive_sequence)
        
#         return longest_consecutive_sequence

        
        
                        






        
        