class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Maintain a running sum - considers whether extending
        # prev sum or starting fresh w/ the current element gives
        # a better result

        # Use variable 'curSum' to track sum of elements
        # At each index, either add current element to curSum or
        # start new subarray by resetting curSum to current element

        # Track maximum at each step and update global max

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub
            

