class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # starting_temperatures = [i for i in range(len(temperatures))]
        warmer_temperatures_dict = {} 
        for i in range(len(temperatures)): 
            warmer_temperatures_dict[i] = 0 

        for i in range(len(temperatures)): 
            current_temperature = temperatures[i]
            start = i + 1
            while (start < len(temperatures)):
                if temperatures[start] > current_temperature:
                    warmer_temperatures_dict[i] = start
                    break
                start += 1 
        result = [] 
        for i in warmer_temperatures_dict:
            if warmer_temperatures_dict[i] > i:
                result.append(warmer_temperatures_dict[i] - i)
            else:
                result.append(0)
            
        return result 