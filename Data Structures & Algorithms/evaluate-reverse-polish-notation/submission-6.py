class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # tokens: A valid arithmetic expression in Reverse Polish Notation
        # Goal: Return the integer that represents the evaluation of the expression

        answer = 0

        # Iterate through tokens
        # If char in tokens is a number, push onto stack
        # If char is an operator, pop off the two numbers from the stack
        # Perform the calculation
        # Push back onto stack

        stack = []

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    answer = a + b
                    stack.append(answer)
                elif t == "-":
                    answer = a - b
                    stack.append(answer)
                elif t == "*":
                    answer = a * b
                    stack.append(answer)
                else:
                    answer = int(float(a / b))
                    stack.append(answer)

            else:
                stack.append(int(t))

        return stack[0]



