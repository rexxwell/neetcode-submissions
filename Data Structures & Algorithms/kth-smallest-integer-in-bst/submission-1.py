from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Brute Force
    Runtime: 64ms
    Memory: 11.2 MB
    Time Complexity:
        Best Case: O(n)
            The helper method takes O(n).
            `.sort()` takes O(n) best case.
        Worst Case: O(nlogn)
            `.sort()` takes O(nlogn) worst case
    Space Complexity: O(n)
        `tree` will always hold n tree nodes.
    n is the number of nodes in the tree.
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
        tree = self.kthSmallestHelper(root, [])
        tree.sort()
        return tree[k - 1]

    def kthSmallestHelper(self, curr: Optional[TreeNode], tree: List[int]) -> List[int]:
        if curr == None:
            return tree

        self.kthSmallestHelper(curr.left, tree)
        self.kthSmallestHelper(curr.right, tree)

        tree.append(curr.val)

        return tree