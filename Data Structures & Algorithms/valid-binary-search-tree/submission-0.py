# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # DFS

        def isValid(node, left, right):

            if not node:
                return True

            if not (left < node.val < right):
                return False

            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        return isValid(root, float("-inf"), float("inf"))

        # BFS
        # Start at root node, check if left < root and right > root

        # if not root:
        #     return True

        # q = collections.deque([(root, float("-inf"), float("inf"))])

        # while q:
        #     node, left, right = q.popleft()

        #     if not (left < node.val < right):
        #         return False

        #     if node.left:
        #         q.append((node.left, left, node.val))
        #     if node.right:
        #         q.append((node.right, node.val, right))

        # return True
