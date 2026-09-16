class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # minHeap
        # restrict minHeap to be k size
        # every time we push a (frequency, value) pair onto the heap, we remove
        # the smallest element to keep the heap at size k

        freq = {}   

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # use minHeap to find top k elements
        
        minHeap = []

        for num in freq.keys():
            heapq.heappush(minHeap, (freq[num], num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res

        