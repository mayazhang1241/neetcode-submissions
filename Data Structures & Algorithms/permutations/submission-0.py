class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Backtracking
        # Iterate through array
        # For each element i in array, append one of the other values
        # Append the other one

        # Base case: If len(subset) == len(nums)
        # Visit one index
        # Backtrack and visit next index

        self.res = []
        self.dfs([], nums, [False] * len(nums)) # marks if visited or not
        return self.res

    def dfs(self, subset: List[int], nums: List[int], picked: List[bool]):
        
        # Base case
        if len(subset) == len(nums):
            self.res.append(subset.copy())
            return

        # Decision
        # If the value has not been visited yet, append it and mark it as visited
        # Once done, backtrack and mark it as unvisited for the next cycle
        for i in range(len(nums)):
            if not picked[i]:
                subset.append(nums[i])
                picked[i] = True
                self.dfs(subset, nums, picked)
                subset.pop()
                picked[i] = False