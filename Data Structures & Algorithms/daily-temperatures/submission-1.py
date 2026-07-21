class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # iterate through temperatures
        # at every i, add that day to the stack
        # if the temp is warmer than the element at the top, pop it off
        # how many days does it take until we need to pop?

        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            
            # if stack not null and current temp is greater than top temp
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd    # number of days
            stack.append((t, i))

        return res