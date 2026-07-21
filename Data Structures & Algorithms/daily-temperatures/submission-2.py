class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = len(temperatures) * [0]
        j = 1
        stack = []

        # iterate through temperatures
        # if the temperature at j is <= temperature at i, j += 1
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index
            stack.append(i)

        return result


