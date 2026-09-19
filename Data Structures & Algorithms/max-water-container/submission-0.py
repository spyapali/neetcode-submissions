class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0  
        while i < j: 
            left_height = heights[i]
            right_height = heights[j]
            max_area = max(max_area, min(left_height, right_height) * (j - i))         
            if left_height > right_height: 
                j -= 1 
            elif right_height > left_height: 
                i += 1 
            else:
                if heights[i + 1] > heights[j - 1]:
                    i += 1  
                else:
                   j -= 1 
        
        return max_area 
                
