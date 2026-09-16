class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use a hashmap
        # loop through
        # at each i, compute target - nums[i]
        # store that result in the map
        # increment i
        # if i is in that hashmap, return the prev index and i

        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i