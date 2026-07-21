class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                popped_index = stack.pop()
                height = heights[popped_index]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea