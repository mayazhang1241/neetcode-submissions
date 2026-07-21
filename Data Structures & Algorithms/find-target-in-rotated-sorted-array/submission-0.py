class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        # Search for the pivot index, or where the array "splits"
        while l < r:

            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l = 0
        r = len(nums) - 1

        # If the target is in the second array, search the second array
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        # Else: search the first array
        else:
            r = pivot - 1

        # Perform binary search to find the target
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
