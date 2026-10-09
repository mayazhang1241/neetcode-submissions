class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # top k most frequent elements
        # if k is 2, then return most frequent element and second most frequent element
        
        # the list is sorted
        # create a frequency map

        freq = defaultdict(list)

        for n in nums:
            if n not in freq:
                freq[n] = 0
            
            freq[n] += 1

        # use a minHeap to return top items easily
        
        minHeap = []
        for n in freq.keys():
            heapq.heappush(minHeap, (freq[n], n))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res



    