class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Given: string of digits (2 - 9)
        # Each digit is mapped to set of characters

        # Return: all possible letter combinations that digits can represent

        # Approach: use a hash map to pair all digits with corresponding letters
        # At each number, you can select one of multiple characters to proceed to
        # the next digit
        # Once done, backtrack to original number and select next character

        # Base condition: stop when i is out of bounds

        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):

            # Base case
            if len(curStr) >= len(digits):
                res.append(curStr)
                return

            # Decision
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
        return res
