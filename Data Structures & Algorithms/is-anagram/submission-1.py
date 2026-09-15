class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sort the letters in the string and compare them

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True

        return False