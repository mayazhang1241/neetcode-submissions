class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # stack
        # iterate through tokens
        # if char in tokens is a number, push onto stack
        # if char is an operator, pop off the two numbers from the stack
        # and perform operation
        # push result back onto stack

        stack = []
        res = 0

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    res = a + b
                    stack.append(res)
                elif t == "*":
                    res = a * b
                    stack.append(res)
                elif t == "-":
                    res = a - b
                    stack.append(res)
                else:
                    res = int(float(a / b))
                    stack.append(res)
            else:
                stack.append(int(t))
        
        return stack[0]
                

