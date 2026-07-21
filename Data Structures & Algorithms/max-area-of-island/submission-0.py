class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Given: 2D matrix of 0s (water) and 1s (land)
        # Island = horizontally or vertically connected 1s, edges surrounded by water
        # Return island w/ most number of cells 

        # Traverse through each cell in the grid
        # If the cell is a 1, perform DFS on it
        # Keep an area variable that increments when the island expands
        # Calculate max of current max and current area 

        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        if not grid:
            return 0

        def dfs(r, c):
            
            # Base case
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea
