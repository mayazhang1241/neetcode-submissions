class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        # Build hashmap 'count1' for string t
        count1 = {}
        for char in t:
            count1[char] = 1 + count1.get(char, 0)

        window = {}     # freq map for sliding window in string s
        letters_needed = len(count1)     # number of letters we need to match
        have = 0     # number of characters who's freq is satisfied

        result = ""
        result_len = float("inf")
        l = 0

        # Expand window with right pointer
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            # If current char satisfies frequency, increment 'have'
            if s[r] in count1 and window[s[r]] == count1[s[r]]:
                have += 1

            while have == letters_needed:

                # If current window is smaller than previous best,
                # update result and result_len
                if (r - l + 1) < result_len:
                    result = s[l:r + 1]
                    result_len = r - l + 1
                
                # Shrink window from left as much as possible
                window[s[l]] -= 1

                # If we accidentally cut out a character in t,
                # stop shrinking the window
                if s[l] in count1 and window[s[l]] < count1[s[l]]:
                    have -= 1
                
                l += 1

        return result







