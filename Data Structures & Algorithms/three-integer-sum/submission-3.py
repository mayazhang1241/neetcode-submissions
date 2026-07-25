class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # given: integery array nums
        # return: ALL triplets nums[i], nums[j], nums[k] where 
        # nums[i] + nums[j] + nums[k] = 0

        # approach: sort the input array
        # for each i, we can use left and right pointers to find j and k pairs
        
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = num + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res





