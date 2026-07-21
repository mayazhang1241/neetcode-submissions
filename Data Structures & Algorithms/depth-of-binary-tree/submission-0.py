# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # traverse through each level
        # when you arrive at node, "pop" off the node and
        # replace with its children
        # increment level
        
        if root is None:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:           # if left child exists
                    queue.append(node.left)
                if node.right:          # if right child exists
                    queue.append(node.right)

            level += 1

        return level
                