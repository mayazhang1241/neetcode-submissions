class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Insert stones into maxHeap 
        # In order to do this, you have to negate all values in
        # stones since heapq only uses minHeap

        # Iterate through maxHeap, pop 2 values (x and y)
        # from the heap at each iteration

        # If x == y, don't insert anything back into
        # the heap

        # If x < y, insert y back into heap with value y - x

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)

        stones.append(0)
        return abs(stones[0])
