from heapq import *

class MedianFinder:

    def __init__(self):
        self.max_heap = []  # left half
        self.min_heap = []  # right half
        # only peek the two heaps' top number to calculate median

    def addNum(self, num: int) -> None:  # 3 * O(log n)
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:  # len(min_heap) > len(max_heap)
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

        # when we have a new number, can't just push into right half
        # must push new number into left half, and pop max number in left half and put it into right half

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):  # even number of elements, find the average of middle two elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

