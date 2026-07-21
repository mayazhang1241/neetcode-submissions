class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Given: 
        #   - 2D array of points called 'points'
        #   - Number of points closest to the origin called 'k'

        # Each element in points is a coordinate [x, y]
        
        # Approach:
        #   - Iterate through array and calculate distances from
        #     each point to origin -> O(n) time
        #   - Store distances in maxHeap
        #   - Since largest item is at top, once size of heap exceeds
        #   - k, remove the top (largest distance) item
        #   - Return all the values in the maxHeap by popping off
        #   - Use heapq library (must negate maxHeap values)

        maxHeap = []
        result = []

        for x, y in points:
            distance = -(x ** 2 + y ** 2)   # Negate bc of maxHeap
            heapq.heappush(maxHeap, [distance, x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            result.append([x, y])

        return result
        