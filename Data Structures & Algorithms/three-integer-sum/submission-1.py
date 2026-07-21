class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums[i] + nums[j] == -nums[k]

        # sort nums
        # iterate through nums
        # fix one number and then search for other 2 using two pointers
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # check for duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res




