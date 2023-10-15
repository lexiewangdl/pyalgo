import heapq
from typing import List
from collections import Counter

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []

        for num, freq in c.items():
            heapq.heappush(heap, (-freq, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)  # O(n) time to determine frequency of each element

        sorted_counter = list(c.items())
        sorted_counter.sort(key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):  # O(k) time to find element and put them in result arr
            result.append(sorted_counter[i][0])

        return result
