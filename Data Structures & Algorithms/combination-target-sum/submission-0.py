class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        total = 0

        def dfs(i, subset, total):

            # Base case
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return

            # If you're able to add on another of the same number you're at
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])

            # If you can't, move on to next number
            subset.pop()
            dfs(i + 1, subset, total)

        dfs(0, [], 0)
        return res

            