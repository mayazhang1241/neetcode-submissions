class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        # Find the row the target is in
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # Find the target in the row

        row = (top + bottom) // 2
        left = 0
        right = cols - 1

        while left <= right:
            middle = (left + right) // 2
            
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        
        return False
        
