class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Given: input of number of queens
        # Return: unique board layout where queens cannot attack each other

        # Queen's surrounding spaces must not have any other queens
        # One queen per row and per column
        # Iterate through columns, make sure no other queens exist in the same row
        # or diagonally

        res = []
        curBoard = [["."] * n for i in range(n)]

        def backtrack(r):

            # Base case: when number of columns == n
            if r == n:
                copy = ["".join(row) for row in curBoard]
                res.append(copy)
                return

            for c in range(n):
                if self.isValidPlacement(r, c, curBoard):
                    curBoard[r][c] = "Q"
                    backtrack(r + 1)
                    curBoard[r][c] = "."

        backtrack(0)
        return res

    def isValidPlacement(self, r: int, c: int, board):

        # Check same column
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
            
        # Check upper left diagonal
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Check upper right diagonal
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True