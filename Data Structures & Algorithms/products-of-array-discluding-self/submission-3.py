class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Given: integer array nums
        # Return: integer array output where each item is 
        #         a product of all the elements of nums except item

        # Keep track of left product and right product
        # Make an array of products of everything to the left of each i
        # Make an array of products of everything to the right of each i

        # left array: product of all numbers to the left of i
        # right array: product of all numbers to the right of i
        
        n = len(nums)
        res = [0] * n
        left = [0] * n
        right = [0] * n

        # first element of left arr and last element of right arr is always
        # 1 since there is nothing

        left[0] = right[n - 1] = 1

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = left[i] * right[i]

        return res


