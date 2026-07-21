"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # begin at random node
        # assign dummy to first input node
        # make current node point to first input node
        # use current to go to neighbors

        # at each node, apend neighbors list to result
        # run dfs on first neighbor

        if not node:
            return None
        
        visited = {}

        def dfs(curr):
            
            if curr in visited:
                return visited[curr]

            clone = Node(curr.val)
            visited[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
            

