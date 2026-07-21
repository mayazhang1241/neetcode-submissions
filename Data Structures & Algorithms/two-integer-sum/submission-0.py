class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i, num in enumerate(nums):
            j_num = target - num

            if j_num in map:
                return [map[j_num], i]

            map[num] = i