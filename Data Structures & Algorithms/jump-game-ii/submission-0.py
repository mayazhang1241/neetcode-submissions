class Solution:
    def jump(self, nums: List[int]) -> int:

        # Create 2 pointers, l and r, to represent window of reachable
        # indices 

        # At each step, iterate through indices in window from l to r 
        # and determine farthest index that can be reached from curr
        # range

        # Update l and r pointers to next range
        # Set l to r + 1 and r to the farthest reachable index

        # Use result variable to keep track of number of min num of
        # steps taken required to reach last index

        # Exit when right pointer goes out of bounds
        
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0

            for  i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res
        