
#        k 
#                 j 
#  i 
#  0  1  2  3  4  5 
# [3, 4, 5, 6, 1, 2], 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1


        while i < j:
            midpoint = i + ((j - i) // 2)

            # the array is sorted 
            if nums[i] < nums[j]:
                return nums[i]
            
            if nums[i] > nums[midpoint]:
                j = midpoint
            else:
                i = midpoint + 1 
      

        return nums[i]
        
        