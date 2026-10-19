class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answers = len(temperatures) * [0]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                colder_index = stack.pop()

                answers[colder_index] = i - colder_index

            stack.append(i)

        return answers