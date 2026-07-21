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
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            # Expanding island
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
        