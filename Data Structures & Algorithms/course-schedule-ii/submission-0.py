class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Detect cycle in graph, use DFS

        # Create adjacency list where prereq[course] contains all of the 
        # prerequisites for a course
        # Ex: prereq = {0: [], 1: [0], 2: [1], 3: [2]}

        prereq = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)

        res = []
        visit = set()   # Marks course as fully safe (no cycles)
        current = set()   # Marks current path (for cycle detection)

        def dfs(course):
            if course in current:  # If course is in current traversal, cycle detected 
                return False
            if course in visit:    # If alr visited, skip over it
                return True

            current.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:   # If course in current ^^
                    return False

            # Remove from current traversal since fully processed
            # and add it to visit (fully processed)
            # Add to result
            current.remove(course)
            visit.add(course)
            res.append(course)
            return True


        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res

