class Solution:
    # Hash Map
    # Runtime: 56ms
    # Memory: 11.2 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n is the length of nums.
    def findDuplicate(self, nums: List[int]) -> int:
        nums_counter = {}

        for num in nums:
            if num in nums_counter:
                return num
            else:
                nums_counter[num] = 0