class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # given integer array nums, return True 
        # hash set since no duplicates

        numbers = set()

        for num in nums:
            if num in numbers:
                return True

            else:
                numbers.add(num)

        return False
        