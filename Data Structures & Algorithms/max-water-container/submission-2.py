class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # given integer array heights
        #   heights[i] = height of the ith bar
        
        # form an area with two heights
        # return the MAX amount of water a container can store

        # two-pointer: l = 0, r = len(heights) - 1
        # calculate the area at each l and r
        #   check to see if heights[l] or heights[r] is greater
        #   width = r - l
        # move the smaller pointer 

        # keep a running MAX and update it every time a larger area is found

        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            current_area = min(heights[l], heights[r]) * (r - l)

            max_area = max(max_area, current_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

            