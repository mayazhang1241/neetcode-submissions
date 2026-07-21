class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # given: integer array nums
        # return: True if any value appears more than once in the array
        #         False otherwise

        # use a hashset to find duplicate characters
        # if the character is already in the hashset, we know it's a
        # duplicate

        # 1. Iterate through nums
        # 2. If nums[i] is in the hashset, return True
        # 3. If the loop finishes and no Trues were returned, return False

        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False