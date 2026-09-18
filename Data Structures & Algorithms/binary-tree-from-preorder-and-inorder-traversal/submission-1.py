# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Array Slicing and `.index()`
    `preorder` goes from root -> left -> right.
    `inorder` goes from left -> root -> right.
    This means `preorder[0]` will always be the `root` of the tree.
    We get the value of the `root` of the tree and then we can lookup
    the index of this node in the `inorder` array where we know that
    elements to the left of it must be elements in the left subtree and
    elements to the right of it must be elements in the right subtree.
    Runtime: 1095ms
    Memory: 40.8 MB
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    n is the length of `preorder` and `inorder`
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        # The root node is always in the start of the `preorder` array.
        node = TreeNode(preorder[0])
        inorder_index = inorder.index(node.val)

        node.left = self.buildTree(preorder[1 : 1 + inorder_index], inorder[:inorder_index])
        node.right = self.buildTree(preorder[1 + inorder_index:], inorder[inorder_index + 1:])

        return node