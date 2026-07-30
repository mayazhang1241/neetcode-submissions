class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # iterate through temperatures
        # for each temperature, store temp, index value pair
        # if the current temp is less than the top of the stack, we 
        # add the value onto the stack

        # if the current temp is > than the top of the stack, we 
        # pop the top of the stack until current temp is < top of the stack
        # compute different between indices and 

        res = len(temperatures) * [0]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                colder_index = stack.pop()
                res[colder_index] = i - colder_index
            
            stack.append(i)

        return res