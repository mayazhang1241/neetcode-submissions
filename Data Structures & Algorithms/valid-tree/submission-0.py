class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # A tree must have exactly n - 1 edges, not valid if not
        if len(edges) != (n - 1):
            return False

        # Create adjacency list mapping neighbors to nodes
        neighbors = {i: [] for i in range(n)}
        for no, nei in edges:
            # Undirected graph, must append both ways
            neighbors[no].append(nei)
            neighbors[nei].append(no)

        visit = set()

        def dfs(node, parent):
            # Already visited, cycle detected
            if node in visit:
                return False

            visit.add(node)
            for neighbor in neighbors[node]:
                if neighbor == parent:
                    continue
                # If neighbor is visited in current node
                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        # Check if all nodes were visited at the end of DFS
        return len(visit) == n