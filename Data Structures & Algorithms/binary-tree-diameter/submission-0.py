# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # diameter = height of left subtree + height of right subtree
        # Depth first search algorithm to calculate height of tree

        diameter = 0

        # Returns height
        def dfs(curr):
            nonlocal diameter

            if curr is None:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter
