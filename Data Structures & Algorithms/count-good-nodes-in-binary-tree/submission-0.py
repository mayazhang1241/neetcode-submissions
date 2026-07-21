# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # DFS recursive search

        # Keep track of maximum value variable and count result

        # If one of the current node's children is larger than
        # the current node, update the max value variable and 
        # increment the count

        def dfs(node, maxVal):

            if not node:
                return 0

            if node.val >= maxVal:
                res = 1
            else:
                res = 0

            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
