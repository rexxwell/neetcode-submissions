class Solution:
    """
    Backtracking (Optimized)

    We have to use a recursive depth-first search so that we never
    generate duplicate combinations.

    At every index `i` in `nums`, we have two decisions:
    1. Include `nums[i]` to the current combination, subtract its
    value from its remaining target, and stay at the same index `i`.
    2. Exclude `nums[i]` from the current combination, leave the
    `target` as it is and move onto the next index `i`.

    Runtime: 167ms
    Memory: 9.6 MB
    Time Complexity: O(2^(T/M) * (T/M))
    Space Complexity: O((T/M) + n)
    T is the target.
    M is the `min(nums)`.
    n is the length of `nums`.
    """

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(2^(T/M) * (T/M))
        Space Complexity: O(m)
        m is the length of `unique_combinations`.
        T is the target.
        M is the `min(nums)`.
        n is the length of `nums`.
        """

        if nums == []:
            return [[]]

        unique_combinations = []
        self.combinationSumHelper(nums, 0, [], target, unique_combinations)
        
        return unique_combinations

    def combinationSumHelper(
        self, 
        nums: List[int], 
        i: int, 
        current_combination: List[int], 
        target: int, 
        unique_combinations: List[List[int]]
    ):
        """
        Time Complexity: O(2^(T/M) * (T/M))
        Space Complexity: O((T/M) + n)
        T is the target.
        M is the `min(nums)`.
        n is the length of `nums`.
        """

        if target == 0:
            unique_combinations.append(current_combination)
            return
        elif target < 0 or i >= len(nums):
            return

        current_combination.append(nums[i])
        self.combinationSumHelper(nums, i, current_combination.copy(), target - nums[i], unique_combinations)
        current_combination.pop()
        self.combinationSumHelper(nums, i + 1, current_combination.copy(), target, unique_combinations)