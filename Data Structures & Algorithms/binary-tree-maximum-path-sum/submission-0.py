# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # Keep track of max path, update every time new max is found

        # If node has left AND right child, calculate current path val
        # Update max path value

        # Use DFS algorithm to calculate

        res = [root.val]

        def dfs(root):

            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If node does not have left or right child, value 
            # of that edge will be set to 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]


        