class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    # Separate array into two halves
    # Smaller half is maxHeap, bigger half is minHeap

    # If arrays are same size, take the max of smaller half and the 
    # min of the bigger half and find the median of those 2

    # If one array is bigger than the other, take the max or min 
    # (depending on which array is bigger)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num) # Larger half
        else:
            heapq.heappush(self.small, -1 * num) # Smaller half

        # Pop largest value from small, push onto large
        if len(self.small) > len(self.large) + 1:
            # Bc minHeap, largest value is located at "bottom"
            val = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, val)
        # Pop smallest value from large, push onto small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2.0
        