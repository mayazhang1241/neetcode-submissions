class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Build adjacency list
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        res = 0

        def dfs(node):
            if node in visit:
                return False

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

