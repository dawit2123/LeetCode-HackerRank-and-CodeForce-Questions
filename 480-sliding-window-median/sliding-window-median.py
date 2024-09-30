import heapq
from collections import defaultdict

class Solution:
    def __init__(self):
        self.small, self.large = [], []  # Two heaps
        self.delayed = defaultdict(int)  # Hashmap to keep track of delayed (removed) elements
        self.small_size, self.large_size = 0, 0  # Size of the two heaps

    def insert(self, num):
        # Insert num into small heap (negative for max-heap behavior)
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.balance()

    def remove(self, num):
        # Mark num for delayed removal
        self.delayed[num] += 1
        
        # Adjust size count accordingly
        if num <= -self.small[0]:
            self.small_size -= 1
        else:
            self.large_size -= 1
        self.balance()

    def balance(self):
        # Rebalance the heaps
        if self.small_size > self.large_size + 1:
            # Move the largest from small to large
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1
        elif self.large_size > self.small_size:
            # Move the smallest from large to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1

        # Clean up top of small heap
        while self.small and self.delayed[-self.small[0]]:
            val = -heapq.heappop(self.small)
            self.delayed[val] -= 1
            if self.delayed[val] == 0:
                del self.delayed[val]

        # Clean up top of large heap
        while self.large and self.delayed[self.large[0]]:
            val = heapq.heappop(self.large)
            self.delayed[val] -= 1
            if self.delayed[val] == 0:
                del self.delayed[val]

    def find_median(self):
        if self.small_size > self.large_size:
            return -self.small[0]
        elif self.large_size > self.small_size:
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0

    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        output = []
        
        # Initialize the first window
        for i in range(k):
            self.insert(nums[i])
        output.append(self.find_median())

        # Slide the window across the array
        for i in range(k, len(nums)):
            self.insert(nums[i])  # Insert the new element
            self.remove(nums[i - k])  # Remove the element that's sliding out
            output.append(self.find_median())  # Append the median

        return output
