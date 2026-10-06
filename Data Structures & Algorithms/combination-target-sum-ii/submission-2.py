class Solution:
    """
    Backtracking

    At each candidate in `candidates`, we have two options:
    1. Include candidate to the `current_combination`, move to the
    next candidate.
    2. Exclude candidate from the `current_combination`, move to the
    next candidate that is different and not a duplicate value so
    that we don't consider the same combinations.

    Runtime: 248ms
    Memory: 10.0 MB
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    n is the length of `candidates`.
    """

    """
    Time Complexity: O(n * 2^n + O(nlogn)) = O(n * 2^n)
    Space Complexity: O(m)
    m is the length of `unique_combinations`.
    n is the length of `candidates`.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        unique_combinations = []
        candidates.sort()
        self.combinationSum2Helper(candidates, target, [], unique_combinations, 0)

        return unique_combinations
        
    """
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    n is the length of `candidates`.
    """
    def combinationSum2Helper(self, candidates: List[int], target: int, current_candidates: List[int], unique_combinations: List[List[int]], i: int) -> None:
        if target == 0:
            unique_combinations.append(current_candidates.copy())

            return
        elif target < 0 or i >= len(candidates):
            return

        current_candidates.append(candidates[i])
        self.combinationSum2Helper(candidates, target - candidates[i], current_candidates, unique_combinations, i + 1)
        current_candidates.pop()
        candidate = candidates[i]

        for j in range(i + 1, len(candidates)):
            if candidate == candidates[j]:
                i += 1

        self.combinationSum2Helper(candidates, target, current_candidates, unique_combinations, i + 1)