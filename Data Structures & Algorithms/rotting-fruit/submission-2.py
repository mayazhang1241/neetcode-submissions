class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        pq = deque()
        minutes = -1
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    pq.append((r, c))

        if fresh == 0:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while pq:
            for q in range(len(pq)):
                r, c = pq.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        pq.append((nr, nc))

            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1



