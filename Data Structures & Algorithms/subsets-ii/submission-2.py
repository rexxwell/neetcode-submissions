class Solution:
    """
    Backtracking

    Runtime: 28ms
    Memory: 8.2 MB
    Time Complexity: O(2^n * n)
    Space Complexity: O(2^n * n)
    n is the length of `nums`.
    """

    """
    Time Complexity: O(nlogn + 2^n * n) = O(2^n * n)
    Space Complexity: O(2^n)
    n is the length of `nums`.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        possible_subsets = []
        nums.sort()
        self.subsetsWithDupHelper(nums, possible_subsets, [], 0)

        return possible_subsets

    """
    Time Complexity: O(2^n * n)
    Space Complexity: O(2^n * n)
    n is the length of `nums`.
    """
    def subsetsWithDupHelper(self, nums: List[int], possible_subsets: List[List[int]], current_subset: List[int], i: int) -> None:
        if i == len(nums):
            possible_subsets.append(current_subset.copy())
            
            return
        
        current_subset.append(nums[i])
        self.subsetsWithDupHelper(nums, possible_subsets, current_subset, i + 1)
        num = nums[i]

        for j in range(i + 1, len(nums)):
            if num == nums[j]:
                i += 1
            else:
                break
        
        current_subset.pop()
        self.subsetsWithDupHelper(nums, possible_subsets, current_subset, i + 1)