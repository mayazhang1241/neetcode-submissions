class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev2, prev1 = 0, 0

        # [prev2, prev1, n, n + 1, n + 2, ...]
        for n in nums:
            temp = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = temp

        return prev1
