# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Depth First Search

    Scenarios:
    1. The maximum path sum includes the left child of the parent.
    2. The maximum path sum includes the right child of the parent.
    3. The maximum path sum includes both the left and right child of the parent,
       with the current node as the connecting node.
    4. The maximum path sum does not include the left and right child of the parent.

    `maxPathSumHelper` function covers scenario 1, 2, and 4 because
    `curr.val + max(left_gain, right_gain)` covers scenario 1, 2, and 4 where
    it chooses if the left or right child is included in the max path sum.
    We cover scenario 4 by defaulting to 0 if `maxPathSumHelper(curr.left)` or
    `maxPathSumHelper(curr.right)` is lesser than 0, then it would be better to
    not choose any of the children and just use the current node to the parent.

    We cover scenario 3 by using a global variable. We have to use a global variable
    here and cannot just do `curr.val + maxPathSumHelper(curr.left) + maxPathSumHelper(curr.right)`
    because by doing the recursive step above, we will break the rules of a path and instead,
    we would be getting the total path sum of the entire tree instead of using the `curr` node
    as a connecting node. So, we have to use a global variable to track it and use
    `curr.val + left_gain + right_gain` where the `curr` node is the apex of the path sum.

    Runtime: 100ms
    Memory: 17.6 MB
    Time Complexity: O(n)
    Space Complexity:
        Worst Case: O(n)
            If the tree is skewed.
        Average/Best Case: O(logn)
            If the tree is balanced.
    n is the number of nodes in the tree.
    """
    global_max_path_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return max(self.maxPathSumHelper(root), self.global_max_path_sum)

    def maxPathSumHelper(self, curr: Optional[TreeNode]) -> int:
        if curr == None:
            return 0

        left_gain = max(0, self.maxPathSumHelper(curr.left))
        right_gain = max(0, self.maxPathSumHelper(curr.right))
        curr_left_right = curr.val + left_gain + right_gain

        if curr_left_right > self.global_max_path_sum:
            self.global_max_path_sum = curr_left_right

        return curr.val + max(left_gain, right_gain)