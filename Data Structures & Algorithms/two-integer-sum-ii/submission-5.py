class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numbers is sorted in non-decreasing order
        # goal: return indices (1-indexed) of 2 numbers index1 and index2

        # index1 + index2 = target, and index1 < index2
        # index1 != index2

        # left and right pointer

        l, r = 0, len(numbers) - 1

        while l < r:
            num_sum = numbers[l] + numbers[r]

            if num_sum < target:
                l += 1
            elif num_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]