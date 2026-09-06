# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BST Property
    # Runtime: 31ms
    # Memory: 8.0 MB
    # Time Complexity:
    #   Worst Case: O(h)
    #       If the BST is skewed, then you will travers through all n nodes or the height h of the tree.
    #   Average Case: O(logh)
    #       If the BST is balanced, the height of the tree is log2(h).
    # Memory Complexity: O(1)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr != None:
            if p.val < curr.val and q.val < curr.val:
                # The lowest common ancestor is on the left.
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                # The lowest common ancestor is on the right.
                curr = curr.right
            else:
                # If one of the nodes is greater than `curr.val` and the other one is lesser than `curr.val`, then that means we have found the lowest common ancestor.
                # If one of the nodes is equal to `curr.val` and the other one is lesser than or greater than, then that means we found the lowest common ancestor!
                return curr