class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Given:
        #   - Unsorted array of ints: nums
        #   - __ largest number in array: k

        # Goal: return kth largest element in SORTED array
        # Solve without sorting

        # Use minHeap using heapq module
        # Once size of minHeap exceeds k, pop off top values
        # Return top value?

        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
