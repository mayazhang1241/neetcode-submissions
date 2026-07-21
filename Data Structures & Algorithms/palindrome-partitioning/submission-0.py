class Solution:

    # To check if string is palindrome, use right and left pointer
    # If str[left] == str[right], left += 1 and right -= 1

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


    def partition(self, s: str) -> List[List[str]]:
        
        # Given a string
        # Return all possible palindromes substrings

        # Write isPalindrome function that returns True if function
        # is palindrome, False otherwise
        
        res = []
        subset = []

        def dfs(j, i):

            # Base case
            # If i == j, it means the last substring checked ended, so
            # subset is valid

            if i >= len(s):
                if i == j:
                    res.append(subset.copy())
                return

            # Decision
            # If current substring is a palindrome in the window s[j : i + 1],
            # add it to current subset
            # Move onto next character that could be another palindrome
            # Backtrack

            if self.isPalindrome(s, j, i):
                subset.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                subset.pop()

            # Whether current window is a valid palindrome or not, try to 
            # extend the end boundary of substring

            # If it is a palindrome, we are looking to see if we can find
            # a longer palindrome
            # If it is not a palindrome, we are looking to see if extending
            # the right boundary will create a palindrome 
            dfs(j, i + 1)

        dfs(0, 0)
        return res


        