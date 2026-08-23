# nums = [1, 2, 4, 6]
# output = [48, 24, 12, 8]

# product from the right 
# product from the left 

# product from the left (forward loop)
# [1, 1, 2, 8]

# product from the right (backward loop)
# [48, 24 ,6 ,1]

# [48, 24 ,6 ,1]
# [1,  1,  2, 8]

# final products: [48, 24, 12, 8] 

# [1, 2, 4, 6]

# first pass solution: 
# def productExceptSelf(self, nums: List[int]) -> List[int]:
#     product = [1 for i in range(len(nums))] 
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i == j:
#                 continue 
#             else:
#                 product[i] *= nums[j]

#     return product  


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_from_right = [1 for i in range(len(nums))] 
        product_from_left = [1 for i in range(len(nums))] 
        product = [1 for i in range(len(nums))] 

        for i in range(1, len(product_from_left)):
            product_from_left[i] = product_from_left[i - 1] * nums[i - 1]
        for i in range(len(product_from_right) - 2, -1, -1):
            product_from_right[i] = product_from_right[i + 1] * nums[i + 1] 
        for i in range(len(product)):
            product[i] = product_from_right[i] * product_from_left[i]
        
        return product 

        