class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        # nums[i] = -(nums[j] - nums[k])
        # -nums[i] = nums[j] + nums[k]

        # iterate through nums
        # at each index, initialize left = j and right = k

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                threeSum = n + nums[j] + nums[k]

                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res

            


