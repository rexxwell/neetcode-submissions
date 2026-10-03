class Solution:
    """
    Backtracking

    Backtracking is visualizing a tree that builds itself forward 
    and then cleans itself up backward.

    In this solution, we are processing each element in order by their index.
    For every number in `nums`, we saying, should we include it in the
    `current_subset` array or not. Since the index gets incremented once,
    each number gets considered exactly once.

    If we trace a small example like `nums = [1]`, notice how we decide,
    should we include `1` or not? So we get two arrays from that, `[]` and `[1]`.
    Notice that is the correct answer to `[1]`? So that means, all unique subsets
    appear at the last level of the tree or recursion stack. This is because
    when we want to make a valid subset for an array of `nums`, what we are doing
    is that we are basically going through each number one by one in the
    `nums` array and we are asking ourself, are we including this number or not?
    After we go through the entire `nums` array with our decisions, we will get
    one valid subset to that `nums` array. So an empty set would be that we excluded
    every number in the `nums` array. So how can we do this in a way where we don't have
    to manually count every single combinations of yes and no's? We can make a recursion
    tree where we ultimately go through every single combination where we get every
    single possibilty of yes and no combinations of `nums` and once we reach the end of
    the array, we would arrive with a valid subset of `nums` and we would append it to
    the final results array. Now, a common point of confusion is when we 
    approved the first index in `nums` and be like, isn't this already a subset of `nums`?
    You are right! It is. But think about it, in the recursion tree, where can we
    get a "valid" subset of just `[nums[0]]`? It is when we approved of including
    the first index and we excluded all the other numbers.

    Runtime: 30ms
    Memory: 8.6 MB
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    n is the length of `nums`.
    """

    """
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    n is the length of `nums`.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        if not nums:
            return subsets

        self.subsetsHelper(0, nums, [], subsets)

        return subsets

    """
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    n is the length of `nums`.

    O(n) in the space complexity comes from `subset + [nums[i]]`
    because we are pretty much making a new copy of a list.

    O(n) in the time in the time complexity comes from making a new copy
    of a list because it has to go through every single element in
    `subset` and `nums[i]` and then make a new copy and add it
    to the `subsets` array.
    """
    def subsetsHelper(self, i, nums, subset, subsets) -> List[List[int]]:
        if i == len(nums):
            subsets.append(subset)
            return

        self.subsetsHelper(i + 1, nums, subset + [nums[i]], subsets)
        self.subsetsHelper(i + 1, nums, subset, subsets)