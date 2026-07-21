"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Given a reference to a node, create a "deep copy" of that node
        # Deep copy: completely independent copy of graph

        # Approach: use hash map to map old nodes to new nodes
        # After making copy of one neighbor, look to see if you 
        # need to make copies of neighbor's neighbors
        # Use DFS to iterate through neighbors

        oldToNew = {}

        def dfs(node):

            # If already made clone, just return that clone
            if node in oldToNew:
                return oldToNew[node]

            # Creating clone
            clone = Node(node.val)
            oldToNew[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node) if node else None

            







