class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # start at root
        # set curr = root
        # if curr < target --> move left
        # if curr > target --> move right
        # do this recursively as you travel down the tree

        # input is list --> root = mid

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1