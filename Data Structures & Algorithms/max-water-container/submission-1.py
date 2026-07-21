class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # keep an overall final max and a current max
        # keep track of length and height
        # left = 0, right = len(heights) - 1
        # if we start at 0 and 7, length = 7 and the min of the two heights
        # (6 and 1) is 1, so we do 1 * 7
        # current max = 7, final max = 7
        # move the pointer that has the smaller height

        final_max, current_max = 0, 0
        l, r = 0, len(heights) - 1

        while l < r:
            current_max = (r - l) * min(heights[l], heights[r])
            final_max = max(final_max, current_max)

            if min(heights[l], heights[r]) == heights[l]:
                l += 1
            elif min(heights[l], heights[r]) == heights[r]:
                r -= 1

        return final_max