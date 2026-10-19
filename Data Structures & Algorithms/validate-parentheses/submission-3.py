class Solution:
    def isValid(self, s: str) -> bool:
        
        # Given string s of opening and closing symbols
        # Determine if s is valid

        symbols = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            
            # If char is a key in symbols (closing symbol)
            if char in symbols:
                # If stack is not empty and the top of the stack matches char's pairing
                if stack and stack[-1] == symbols[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False



