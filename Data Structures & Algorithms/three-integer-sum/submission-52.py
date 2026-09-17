
#          k                     
#        j 
#      i  
# [-4,-1,0,1,2]

# [-1, 1, 2], [-1, 0, 1]

#    k 
#        j 
#  i 
# [0, 1, 1]

#  - K starts based on whether we need a positive number or a negative number
#  - if K needs to be less than i, or K needs to be greater than J, then see whether the sum is greater or less than zero. If greater than 0, decrement J, if less than 0, increment i. 
#  - otherwise, if i + j is greater than zero, decrement J. 

#                
#   i              j 
# [-4, -1, -1, 0,1,2]
# left_num = -4 
# right_num = 2 
# addition = -2 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = {}  
        for i in range(len(nums)):
            num = nums[i]
            k, j = i + 1, len(nums) - 1 
            while k < j:
                s = nums[k] + nums[j] + nums[i]
                if s < 0:
                    k += 1 
                elif s > 0: 
                    j -= 1 
                else:
                    value = tuple((nums[i], nums[k], nums[j]))
                    if value in result:
                        result[value].append(tuple((i, k, j)))
                    else:
                        result[value] = [tuple((i, k, j))]
                    k += 1 
                    j -= 1   
        triplets = [] 
        for value in result:
            indices = result[value]
            for index in indices: 
                if index[0] != index[1] != index[2]:
                    triplets.append([value[0], value[1], value[2]])
                    break 
                
        return triplets          
                









        