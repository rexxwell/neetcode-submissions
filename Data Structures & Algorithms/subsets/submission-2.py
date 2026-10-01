class Solution:
    """
    Brute Force
    Runtime: 45ms
    Memory: 8.7 MB
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    n is the length of `nums`.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        if not nums:
            return result
        
        for num in nums:
            result += [curr + [num] for curr in result] 

        return result