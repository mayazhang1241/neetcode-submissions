class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Build adjacency list
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()   # Keeps tracks of nodes we've explored via DFS
        res = 0

        def dfs(node):
            # If node is already in a component, don't explore
            if node in visit:
                return

            # Mark node as visited, run DFS on all of its neighbors
            visit.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        # Iterate through all nodes, if node is not in visited, run DFS on it
        # Node not being in visited means it is disconnected from prev components
        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1

        return res

