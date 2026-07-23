class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two-pointer
        # return [l, r] such that numbers[l] + numbers[r] = target
        
        res = []
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                res.append(l + 1)
                res.append(r + 1)
                return res
