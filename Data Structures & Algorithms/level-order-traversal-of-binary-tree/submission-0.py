# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # BFS
        # Start at root
        # Store nodes in queue
        # When you reach a new node, you check to see if left and right exist
        # If they do, enqueue those nodes
        # Dequeue the next node and search its subtrees

        result = []
        q = collections.deque()
        
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                result.append(level)

        return result

