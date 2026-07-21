class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # minHeap: every time the list grows more than k elements, we pop that item

        occurrences = {}
        for num in nums:
            if num not in occurrences:
                occurrences[num] = 0
            occurrences[num] += 1

        minHeap = []
        for num in occurrences.keys():
            heapq.heappush(minHeap, (occurrences[num], num))
        
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result