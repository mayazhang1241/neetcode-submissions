class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # For each num in nums, you have the choice to either add to existing array or 
        # add to empty array

        # Base case: When index is out of bounds
        # Decision: add num to result, explore other options, pop it off


        res = []
        subset = []

        def dfs(i):

            # Base case
            if i == len(nums):
                res.append(subset.copy())
                return

            # Decision 1: add to existing array
            subset.append(nums[i])
            dfs(i + 1)

            # Decision 2: add to empty array
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
