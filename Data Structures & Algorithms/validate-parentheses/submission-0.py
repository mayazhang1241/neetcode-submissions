class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # Use a dictionary to map closing brackets to matching open brackets
        bracket_dict = { ')' : '(', '}' : '{', ']' : '[' }

        for char in s:
            if char in bracket_dict:
                if stack and stack[-1] == bracket_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        # If everything matches correctly, the stack should be empty
        if not stack:
            return True
        else:
            return False