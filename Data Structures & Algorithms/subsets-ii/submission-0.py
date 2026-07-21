class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # Given array nums
        # Return all possible subsets
        # Rules: cannot contain duplicate subsets
        # To combat this, sort the array first
        # If duplicate element occurs, skip past it


        # Base case: if index is out of bounds
        
        res = []
        subset = []
        
        nums.sort()

        def dfs(i):

            # Base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res