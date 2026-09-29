class MedianFinder:
    """
    Brute Force (List)
    Runtime: 394ms
    Memory: 13.3 MB
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    n is the length of `self.nums`.
    """

    def __init__(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(n)
        n is the length of `self.nums`.
        """

        self.nums = []

    def addNum(self, num: int) -> None:
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        n is the length of `self.nums`.
        """

        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """

        if len(self.nums) % 2 == 0:
            return (self.nums[len(self.nums) // 2] + self.nums[(len(self.nums) - 1) // 2]) / 2
        else:
            return self.nums[len(self.nums) // 2]