class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Given array prerequisites
        # Given number of required courses
        # [0, 1] means you take course 1 before you can take course 0

        # Think of the courses as edges ([a, b]: a -> b)
        # If the graph contains a cycle, then return False

        # DFS: if you visit a node that has already been visited and is not the parent node,
        # there is a cycle

        # 1. Build a graph from prerequisites array
        # 2. Track the visit state of each node
        #    0 = unvisited
        #    -1 = visiting 
        #    1 = visited
        # If you visit a -1 node, a cycle is detected -> return False


        # Build the graph
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses


        def dfs(course):
            if visited[course] == -1:   # Cycle detected
                return False
            if visited[course] == 1:    # Fully explored, no cycles
                return True

            visited[course] = -1    # Mark course as visiting

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 1
            return True


        # Visit each course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        
        