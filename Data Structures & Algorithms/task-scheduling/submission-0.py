class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Given:
        #   - Array of CPU tasks: tasks
        #   - Each task is an uppercase English character A-Z
        #   - Number of CPU cycles needed: n

        # Goal: return minimum number of CPU cycles required

        # A cycle is defined as either a letter or 'Idle'
        # If two tasks are identical, meaning they're the same letter,
        # they must be separated by n cycles
        # This could mean a combination of letters and 'Idle's, just 
        # letters, or just 'Idle's, but it must be n cycles

        # Use maxHeap using heapq module to sort frequencies of letters
        # Must negate values since using maxHeap
        # Use time counter to keep track of time
        # Use queue to keep track of updated frequencies and time

        # Each task represents 1 unit of time
        # Minimize idle time

        # Return the time counter

        # O(n * m)  m represents idle time

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q: 
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)    # Add 1 bc negative
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time



