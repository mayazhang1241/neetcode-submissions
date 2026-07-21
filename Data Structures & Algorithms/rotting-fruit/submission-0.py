class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Given 2D matrix of 0s, 1s, and 2s
        # Each minute, if a fresh fruit is adjacent to a rotten fruit, 
        # then fresh fruit also becomes rotten 
        # Return minimum number of minutes that must pass until there is no fresh fruit

        # Use BFS since we need to explore level-by-level, not by depth
        # We need to determine which fruits rot at each second
        # At each second, we "rot" the fruit that is adjacent to the rotten fruit
        # The time that a fruit becomes rotten is the level at which it is visited

        # Each minute represents a level in BFS
        # For each rotten fruit at the current minute, rot all of its adjacent fresh fruits

        q = collections.deque()
        fresh = 0
        time = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and 
                        col in range(cols) and 
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1
