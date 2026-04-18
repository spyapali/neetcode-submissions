# nums = [1,2,2,3,3,3]
# k = 2
# frequencies = {1:1, 2:2, 3:3} 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {} 
        for num in nums: 
            if num not in frequencies: 
                frequencies[num] = 1
            else: 
                frequencies[num] += 1 
        
        sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1])
        sorted_values = [k[0] for k in sorted_frequencies]
        top_frequent_items_count = k 
        top_k_elements = [] 
        while top_frequent_items_count > 0:
            top_k_elements.append(sorted_values.pop())
            top_frequent_items_count -= 1; 
        
        return top_k_elements








        