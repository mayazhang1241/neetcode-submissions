class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # the operand for the two numbers comes after the second number
        # iterate through tokens
        # when you come across a number, add it to the stack
        # if you come across an operator, pop the two numbers off the stack
        # perform the operation
        # push result back onto the stack
        # do this until the stack is empty 

        stack = []
        res = 0

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()
                
                if token == '+':
                    res = num1 + num2
                    stack.append(res)
                elif token == '-':
                    res = num2 - num1
                    stack.append(res)
                elif token == '*':
                    res = num1 * num2
                    stack.append(res)
                else:
                    res = int(float(num2 / num1))
                    stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]



