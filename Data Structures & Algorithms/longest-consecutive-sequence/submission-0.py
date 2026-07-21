class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest_count = 0

        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                while (num + count) in numSet:
                    count += 1
                longest_count = max(count, longest_count)
        
        return longest_count