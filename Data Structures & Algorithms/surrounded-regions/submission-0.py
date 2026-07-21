class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # Given 2D matrix of X's and O's
        # Change all surrounded O regions to X's, modify the board in-place

        # Approach: DFS
        # Surrounded regions must not be touching any O that is on the border
        # O's on the border should not be able to connect to any O's in the grid
        # Start from border and mark regions that are reachable by the border O's

        # 1. (DFS) Capture unsurrounded regions (O -> M)
        # 2. Capture surrounded regions (O -> X)
        # 3. Uncapture unsurrounded regions (M -> O)

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O"):
                return

            board[r][c] = "M"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            # First column
            if board[r][0] == "O":
                dfs(r, 0)

            # Last column
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            # First row
            if board[0][c] == "O":
                dfs(0, c)

            # Last row
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "M":
                    board[r][c] = "O"




