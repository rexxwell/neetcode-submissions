class Solution:
    """
    Backtracking

    Permutation is when order matters. For permutation, we cannot
    use the binary decision tree on whether we decide to include a
    number or not because each elemnt does not have a fixed yes/no
    decision from left to right.

    In permutation, the first slot has N options where N is the length
    of `nums`. The second slot has N - 1 options and so on. So, we make
    a for loop which considers the first element in the first slot and then
    recurse the function where it knows that the first element is already
    in the first slot and it would consider the second one now. That recursion
    stack would keep going until the first permutation is appended to
    `possible_permutations`, then it would pop the first element that was
    added to the `current_permutation` and then consider the second element
    as the first slot. This would would keep going until we considered
    every element in every slot.

    Runtime: 44ms
    Memory: 8.5 MB
    Time Complexity: O(n * n!)
    Space Complexity: O(n * n!)
    n is the length of `nums`.
    """

    """
    Time Complexity: O(n * n!)
    Space Complexity: O(n! + n)
    n is the length of `nums`.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        possible_permutations = []
        nums_flags = [False] * len(nums)
        self.permuteHelper(
            nums, 
            possible_permutations, 
            nums_flags, 
            []
        )

        return possible_permutations

    """
    Time Complexity: O(n * n!) 
    Space Complexity: O(n * n!)
    n is the length of `nums`.
    """
    def permuteHelper(
        self, 
        nums: List[int], 
        possible_permutations: List[List[int]], 
        nums_flags: List[bool], 
        current_permutation: List[int]
    ) -> None:
        if len(current_permutation) == len(nums):
            possible_permutations.append(current_permutation.copy())
            
            return
        
        for i in range(len(nums)):
            if not nums_flags[i]:
                current_permutation.append(nums[i])
                nums_flags[i] = True
                self.permuteHelper(nums, possible_permutations, nums_flags, current_permutation)
                current_permutation.pop()
                nums_flags[i] = False