class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # Given: 2D grid of heights
        # heights[r][c] represents the height above sea level of (r, c)
        # Pacific ocean from the top and left sides

        # Find all cells where water can flow from that cell to both oceans
        # Return as a 2D list where each element is a list [r, c]

        # Approach: DFS
        # Iterate through border cells 
        # See which other cells adjacent to the border cells can reach other ocean
        # If any adjacent cells have height <= current cell's height, 

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == rows or c == cols or 
                heights[r][c] < prevHeight
            ):
                return
            
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for c in range(cols):
            # First row, Pacific Ocean
            dfs(0, c, pac, heights[0][c])

            # Last row, Atlantic Ocean
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            # First col, Pacific Ocean
            dfs(r, 0, pac, heights[r][0])

            # Last row, Atlantic Ocean
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

