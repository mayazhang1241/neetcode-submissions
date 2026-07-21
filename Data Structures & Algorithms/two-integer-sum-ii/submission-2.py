class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # given: numbers, sorted in non-decreasing order
        # [1, 2, 3, 4]
        # return: [index1, index2]
        # index1 and index2 must add up to target, index1 < index2,
        # index1 != index2

        # because it is sorted, we can compute index1 + index2 at each
        # right and left index
        # if the sum is bigger than target, right -= 1
        # if the sum is less than the target, left += 1 

        left, right = 0, len(numbers) - 1
        res = []

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
            

        