class KthLargest:

    # Use heapq module to initialize minHeap
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # Trim minHeap so that it only contains k largest 
        # elements 

        # Aka minHeap[0] is now the k-th largest overall number
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        # Push values onto minHeap
        heapq.heappush(self.minHeap, val)

        # Smallest val located at last item in minHeap
        # If the length of minHeap exceeds k, pop off smallest val
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return largest value at minHeap, which is located at
        # the beginning
        return self.minHeap[0]
