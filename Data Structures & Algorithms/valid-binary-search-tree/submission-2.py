# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Depth First Search
    # Runtime: 82ms
    # Memory: 13.3 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Worst Case: O(n)
    #       If the tree is skewed.
    #   Average/Best Case: O(logn)
    #       If the tree is balanced or perfectly balanced.
    # n is the number of nodes in the tree.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, curr: Optional[TreeNode], lower_limit: int, upper_limit: int) -> bool:
        if curr == None:
            return True

        if not (lower_limit < curr.val < upper_limit):
            return False

        return self.isValidBSTHelper(curr.left, lower_limit, curr.val) and self.isValidBSTHelper(curr.right, curr.val, upper_limit)