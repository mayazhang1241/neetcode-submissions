# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Root is always first item in preorder
        # Find index that root is at in inorder
        # Everything to left of that index is left subtree
        # Everything to right of that index is right subtree


        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0]) # size of left subtree

        # preorder[1 : idx + 1] = next idx values in preorder must be
        # in left subtree
        # inorder[:idx] = all elements before root value in inorder
        root.left = self.buildTree(preorder[1 : idx + 1], inorder[:idx])

        # preorder[idx + 1 :] = all values after root and left subtree
        # must be in right subtree
        # inorder[idx + 1 :] = everything after root node in inorder
        # must be in right subtree
        root.right = self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :])

        return root
        