# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Write dfs subfunction that returns height at each node
        # When calculating heights, also check if current node is
        # balanced

        # If (abs(left.height - right.height)) > 1, update global
        # variable 'isBalanced' to be True or False

        # Value of 'isBalanced' indicates whether entire tree is
        # balanced or not

        # [bool isBalanced, height of tree]

        def dfs(root):
            if root is None:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            # If left subtree is True (balanced) and 
            # right subtree is True (balanced) and the difference
            # of the heights is <= 1, isBalanced = True

            isBalanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # height = 1 + max(left height, right height)
            return [isBalanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
            

        