class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # For each element in array, use abs value to find index and mark as negative
        # When iterating through, if a number has a negative index, it means
        # the number is a duplicate and we can return False

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1

        return -1