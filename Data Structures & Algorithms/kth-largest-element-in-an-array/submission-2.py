class Solution:
    """
    Brute Force (Sorting)
    Runtime: 136ms
    Memory: 12.8 MB
    Time Complexity: O(nlogn)
    Space Complexity: O(n) total space, O(1) auxiliary space
    n is the length of `nums`.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]