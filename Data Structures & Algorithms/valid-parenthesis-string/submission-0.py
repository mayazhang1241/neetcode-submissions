class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # Maintain 2 stacks: one for left parantheses ( and one for stars *
        # Each time you come across a right paranthesis ), pop either a left
        # parantheses or a star off one of the stacks

        # If left parentheses stack is empty, return True
        # Doesn't matter if star stack is empty or not bc stars can also be 
        # empty strings, so it's still valid

        # If left parentheses stack is NOT empty, try to match w/ remaining stars 
        # and pop both off at the same time
        # If left parenthesis index > *, return false 

        left = []
        star = []

        for i, char in enumerate(s):
            if char == '(':
                left.append(i)
            elif char == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False

        return not left
