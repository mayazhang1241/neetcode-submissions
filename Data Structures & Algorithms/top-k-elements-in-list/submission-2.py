class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use a hashmap to build frequency map
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1

        # {1 : 1
        #  2 : 2
        #  3 : 2}

        # use a minHeap to find the top k elements
        # Sort the keys
        # Smallest element = element with the least frequencies, so it
        # will get popped
        minHeap = []

        for num in frequencies.keys():
            # Push onto heap as a tuple (frequency, num) so that the 
            # minHeap will sort first by frequency, then by number
            heapq.heappush(minHeap, (frequencies[num], num))

            # Smallest element = element with the least frequencies, so it
            # will get popped
            # Don't let the list grow bigger than k
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # we need the number from the tuples of the minHeap
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res







