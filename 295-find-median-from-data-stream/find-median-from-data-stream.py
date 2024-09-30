class MedianFinder:

    def __init__(self):
        self.small_heap, self.large_heap=[],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -1*num)
        # checking if it's placed in wrong position by it's value
        if (self.small_heap and self.large_heap and -1 * self.small_heap[0] > self.large_heap[0]):
            val= -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        # checking for the number of values between the two heaps
        if (len(self.small_heap)-len(self.large_heap))>1:
            val=-1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        if (len(self.large_heap)-len(self.small_heap))>1:
            val= heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        elif len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]
        return (-1 * self.small_heap[0] + self.large_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()