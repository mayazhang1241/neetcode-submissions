class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # Given: 2D grid of -1s, 0s, and INFs
        # Fill each land cell (INF) with distance to nearest treasure chest
        # If land cell cannot reach treasure chest, keep it as INF
        # Can only go up, down, left, or right

        # Approach: iterate through each cell of grid
        # Bc it's a 2D grid, need rows and columns

        # Use DFS
        # Start from treasure chest, not INF
        # There are multiple treasure chests and we are trying to find the shortest path
        

        if not grid or not grid[0]:
            return

        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, distance):

            # If out of bounds or it's not a shorter path, stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] < distance:
                return 

            grid[r][c] = distance
            for dr, dc in directions:
                dfs(r + dr, c + dc, distance + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    for dr, dc in directions:
                        dfs(r + dr, c + dc, 1)