class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Given a 2D grid of characters and a word
        # Return true if the word is present in the grid, else return false

        # Base case: if substring variable == word
        # Decision: If current character matches character of word, backtrack 
        # and check all around for next character
        # If not, move onto next character in board
        # At each step, add cell to a hash set to avoid visiting it again

        # Grid is size 5 x 3

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):

            # Base case:
            if i == len(word):
                return True

            # If out of bounds or doesn't match with word
            if (min(r, c) < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in visited):
                return False

            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False






