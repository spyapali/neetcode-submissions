class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {} 
        # add values to numbers dictionary 
        for i in range(len(nums)):
            num = nums[i]
            if num not in numbers:
                numbers[num] = [i]
            else:
                numbers[num].append(i)

        # loop through the array and return the indices
        for i in range(len(nums)):
            current_num = nums[i]
            difference = target - current_num 
            if difference in numbers:
                indices = numbers[difference]
                for index in indices: 
                    if index != i:
                        return [i, index]

         
     
        
        