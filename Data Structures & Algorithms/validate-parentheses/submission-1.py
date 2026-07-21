class Solution:
    def isValid(self, s: str) -> bool:
        
        # every time you encounter an open bracket, push onto stack
        # when you encounter a closing bracket, pop from stack and see if 
        # they pair together
        # if the stack is empty, then everything was valid

        stack = []
        pairs = { '(': ')', '[': ']', '{': '}' }

        for char in s:
            if char == '(':
                stack.append('(')
            elif char == '[':
                stack.append('[')
            elif char == '{':
                stack.append('{')

            if char == ')' or char == ']' or char == '}':
                if stack and pairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return not stack
                    