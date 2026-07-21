# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Traverse through main tree
        # At each node, check if subtree at that node is identical to param subRoot

        # Edge cases
        if not root:
            return False
        if not subRoot:
            return False

        # Go to sameTree function to check if 'subroot' is a subtree in 'root'
        if self.sameTree(root, subRoot):
            return True

        # Recursively call function back to check each node of 'root'
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True

        # Check if left and right nodes are equivalent
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

        return False

        