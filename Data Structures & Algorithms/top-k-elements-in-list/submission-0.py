class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,2,2,3,3,3], k = 2
        # brute force way of doing this: 
        # 1. Create a map 
        # 2. Loop through the array, and grab the top-most values in the array. 
        frequencies = {}
        for num in nums: # O(N)
            if num in frequencies:
                frequencies[num] += 1 
            else:
                frequencies[num] = 0 
        print(frequencies)
        # sort the values based on the frequencies within the frequencies map. 
        values_descending = sorted(frequencies, key=frequencies.get, reverse=True)
        most_frequent_numbers = [] 
        for i in range(k):
            value = values_descending[i]
            most_frequent_numbers.append(value)
        return most_frequent_numbers

