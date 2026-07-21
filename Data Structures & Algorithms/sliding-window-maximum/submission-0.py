class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        max_heap = []

        for i in range(len(nums)):

            # Must convert numbers to negative because heapq is
            # by default a min heap
            heapq.heappush(max_heap, (-nums[i], i))

            # Once we have at least k elements in the window
            if i >= k - 1:

                # Remove elements from heap that are outside window
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)

                # Convert results back to positive
                result.append(-max_heap[0][0])

        return result