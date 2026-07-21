class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Start at index 0
        # Move forward the number of spaces in the array that the
        # current index indicates
        # If we reach the end, return True
        # Else, return False

        goal = len(nums) - 1

        # Iterate backward over a list excluding last item
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0