import heapq


class MedianFinder:
    """
    Min and Max Heap
    Runtime: 97ms
    Memory: 13.6 MB
    Time Complexity: O(logn)
    Space Complexity: O(n)
    n is the number of numbers added via `addNum`.
    """

    def __init__(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(n/2 + n/2) = O(n)
        n is the number of nums.
        """

        self.left_half_nums = []
        self.right_half_nums = []

    def addNum(self, num: int) -> None:
        """
        Time Complexity: O(log(n/2)) = O(logn)
        Space Complexity: O(1)
        n is the number of nums.
        """

        if len(self.left_half_nums) == 0 and len(self.right_half_nums) == 0:
            # If the min and max heap are both empty, then just
            # add it to the max heap (`left_half_nums`).
            heapq.heappush(self.left_half_nums, -num)
        elif len(self.right_half_nums) == 0 and num > -self.left_half_nums[0]:
            # If the min heap (`right_half_nums`) is empty and the num
            # is greater than the maximum num in `left_half_nums`, then it
            # belongs to the `right_half_nums`.
            heapq.heappush(self.right_half_nums, num)
        elif len(self.right_half_nums) >= 1 and num > self.right_half_nums[0]:
            # If the min heap (`right_half_nums`) is not empty and the num
            # is greater than the minimum num in `right_half_nums`, then it belongs
            # to the `right_half_nums`.
            heapq.heappush(self.right_half_nums, num)
        else:
            # Else, we push num to the `left_half_nums`.
            heapq.heappush(self.left_half_nums, -num)
        
        # If the size difference between the two heaps become greater than one,
        # then we rebalance them by popping an element from the bigger heap and
        # adding it to the smaller heap.
        if abs(len(self.left_half_nums) - len(self.right_half_nums)) > 1:
            if len(self.left_half_nums) > len(self.right_half_nums):
                heapq.heappush(self.right_half_nums, -heapq.heappop(self.left_half_nums))
            else:
                heapq.heappush(self.left_half_nums, -heapq.heappop(self.right_half_nums))    

    def findMedian(self) -> float:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """

        if (len(self.left_half_nums) + len(self.right_half_nums)) % 2 == 0:
            return (-self.left_half_nums[0] + self.right_half_nums[0]) / 2
        else:
            if len(self.left_half_nums) > len(self.right_half_nums):
                return -self.left_half_nums[0]
            else:
                return self.right_half_nums[0]