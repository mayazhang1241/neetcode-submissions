class Solution:
    def isValid(self, s: str) -> bool:
        
        characters = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in characters:
                if stack and stack[-1] == characters[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False