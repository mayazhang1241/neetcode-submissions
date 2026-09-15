class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # is the array sorted?
        nums.sort()

        # edge case: if there is only one item in the array
        if len(nums) == 1:
            return False

        # loop through nums with index i
        # if nums[i - 1] == nums[i] --> return True
        # otherwise return false

        for i in range(len(nums)):
            if nums[i - 1] == nums[i]:
                return True

        return False