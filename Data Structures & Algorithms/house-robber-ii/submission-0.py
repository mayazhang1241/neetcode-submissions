class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # run house robber 1 on arrays:
        # [house[1] : house[n - 2]]
        # [house[2]: house[n - 1]]

        # nums[0] accounts for edge case: only one house in array
        return max(nums[0], self.houseRobberOne(nums[1:]), self.houseRobberOne(nums[:-1]))


    def houseRobberOne(self, nums):
        prev2, prev1 = 0, 0

        for n in nums:
            temp = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = temp

        return prev1