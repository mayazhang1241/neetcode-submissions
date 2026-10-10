class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # elements do NOT have to be consecutive in original array -> sort it?
        # duplicates are ignored

        # edge case: if array is empty, max streak is 0
        if not nums:
            return 0

        # [0,3,2,5,4,6,1,1]
        # 1. sort it
        nums.sort()

        current_max = 1
        overall_max = 1

        # [0, 1, 1, 2, 3, 4, 5, 6]
        # 2. iterate through nums
        # 3. there are 2 conditions: 
        #       1. nums[i] != nums[i - 1]
        #       2. nums[i] == nums[i - 1] + 1
        #       put these in a while loop
        #       break if conditions aren't met
        #       store result in current_max

        for i in range(1, len(nums)):
            # ignore duplicates
            if nums[i] == nums[i - 1]:
                continue

            # check that it's part of consecutive sequence
            if nums[i] == nums[i - 1] + 1:
                current_max += 1
            else:
                # sequence is broken -> reset current_max to 1
                current_max = 1

            overall_max = max(overall_max, current_max)

        return overall_max



        


        


        

        