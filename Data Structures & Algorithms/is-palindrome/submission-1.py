class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # brute force
        # initialize a right and left pointer
        l, r = 0, len(s) - 1

        # while the left pointer is less than the right pointer:
        while l < r:
            # move past characters that are not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True