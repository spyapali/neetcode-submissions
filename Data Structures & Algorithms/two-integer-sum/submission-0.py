class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)):
            current_num = nums[i]
            diff = target - current_num
            if diff in seen and seen[diff] != i:
                return [seen[diff], i]
            seen[current_num] = i
                