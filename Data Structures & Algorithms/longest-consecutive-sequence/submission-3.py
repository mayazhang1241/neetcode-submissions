class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Input: [2,20,4,10,3,4,5]
        # Return: length of longest consecutive sequence of elements

        # Consecutive sequence = sequence of elements in which each
        # element is exactly 1 greater than the previous element
        # Do NOT have to be consecutive in the original array

        # sort nums
        # iterate through nums
        # start the "streak" at 0
        
        if not nums:
            return 0
        
        current_streak = 0
        expected = nums[0]
        res = 0
        i = 0

        nums.sort()

        # expected = the expected number we want to see

        while i < len(nums):
            if expected != nums[i]:
                expected = nums[i]
                current_streak = 0

            # skips past duplicate values
            while i < len(nums) and expected == nums[i]:
                i += 1
                
            current_streak += 1
            expected += 1
            res = max(res, current_streak)

        return res








        