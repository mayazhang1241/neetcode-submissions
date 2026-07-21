class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # given: array nums
        # question: is it sorted?
        # answer: no

        # return [[nums[i], nums[j], nums[k], [nums[i], nums[j], nums[k], ...]
        # where nums[i] + nums[j] + nums[k] == 0
        # i.e., nums[i] = -(nums[j] + nums[k])

        # sort nums
        # [-1,0,1,2,-1,-4] --> [-4, -1, -1, 0, 1, 2]
        nums.sort()

        # as we sort through nums with index i, can we find j and k pairs?
        # at each i, have j = i + 1 and k = len(nums) - 1
        
        res = []

        for i, num in enumerate(nums):
            # if beginning number in nums is a 0, then end early because
            # everything else is positive and won't add to 0
            if num > 0:
                break

            # ensures duplicates don't exist
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # j and k, respectively
            while left < right:
                sum = num + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -=1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
                
            

            
            

