class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # Sort intervals by start value
        # Process queries in increasing order

        # Add intervals to minHeap while start values are <= query
        # Store end values and sizes

        # Remove elements from heap while top's end value is 
        # less than current query

        # Output is top's size if heap is non-empty (otherwise -1)

        intervals.sort()
        minHeap = []
        result, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # Push end values and sizes onto heap
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # while end value on heap is less than query, pop off heap
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Result is at top of minHeap
            result[q] = minHeap[0][0] if minHeap else -1

        return [result[q] for q in queries]

                


