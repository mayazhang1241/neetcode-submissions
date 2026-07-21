class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Given: 9 x 9 sudoku board
        # to check duplicates, use a hashset()

        # need one hashset to check rows, one 

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                box_key = (r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True