class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Given 2D grid of 0s and 1s
        # Island = connection of land (or 1s), all edges are surrounded by water
        # Return number of islands in grid

        # Approach: DFS
        # Iterate through each cell in the grid
        # If cell == 1, explore further until there are 0's all around
        # Mark visited land cells as 0 so that we don't revisit since they belong
        # to same island

        # Since grid is a 2D array, must iterate through cells with format grid[r][c]
        # Since 1s can only be connected horizontally or vertically to be considered
        # an island, must define directions


        # Edge case: empty grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):

            # Base case
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0' or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
        