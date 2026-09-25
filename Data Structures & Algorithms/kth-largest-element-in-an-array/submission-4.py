import heapq

class Solution:
    """
    Max Heap
    Runtime: 175ms
    Memory: 12.5 MB
    Time Complexity: O(n + klogn)
    Space Complexity: O(n)
    n is the length of `nums`.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)

        for i in range(k - 1):
            heapq.heappop(max_heap)

        return -max_heap[0]