class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix suffix
        # prefix[i] stores aggregate (sum, product, min, max) of all elements from index 0 to i-1
        # suffix[i] stores aggregate of all elements from index i + 1 to n - 1

        n = len(nums)
        res = [1] * n

        # calculate prefix products (left to right)
        prefix = 1
        
        for i in range(n):
            res[i] = prefix     # store left product
            prefix *= nums[i]       # update running product for next item

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
