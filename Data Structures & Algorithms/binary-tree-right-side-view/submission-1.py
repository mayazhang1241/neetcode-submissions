# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # BFS recursive search only for right side

        # Initialize result array
        # Start at root node, traverse tree level by level

        # Once we completely visit a level, take the last node of 
        # that level and add it to result

        res = []
        q = collections.deque([root])

        while q:
            rightSide = None

            for i in range(len(q)):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res




