from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Depth First Search
    Runtime: 56ms
    Memory: 11.5 MB
    Time Complexity:
        Worst Case: O(n)
        Average/Best Case: O(logn + k)
    Space Complexity:
        Worst Case: O(n)
            If the tree is skewed.
        Average/Best Case: O(logn)
            If the tree is balanced.
    n is the number of nodes in the tree.
    '''
    
    def __init__(self):
        self.i = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> Optional[int]:    
        if root == None:
            return None

        left = self.kthSmallest(root.left, k)

        if left != None:
            return left

        self.i += 1

        if self.i == k:
            return root.val

        right = self.kthSmallest(root.right, k)

        if right != None:
            return right

        return None