class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # brute force
        n = len(nums)
        res = [0] * n

        # for each index i from 0 to the end of len(nums) - 1:
        # initialize a current product = 1
        # loop through all indices j from 0 to len(nums) - 1
        # if j != i, multiply product by nums[j]
        # store product in res[i]

        for i in range(n):
            product = 1

            for j in range(n):
                if j != i:
                    product *= nums[j]
            
            res[i] = product

        return res


        # 
        