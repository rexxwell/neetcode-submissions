class Solution:
    # Brute Force
    # Runtime: 2597ms
    # Memory: 11.6 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num_i = nums[i]

            for j in range(i + 1, len(nums)):
                num_j = nums[j]

                if num_i == num_j:
                    return num_i