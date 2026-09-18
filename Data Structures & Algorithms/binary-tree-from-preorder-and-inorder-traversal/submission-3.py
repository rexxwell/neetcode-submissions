# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Hash map and two pointers.
    Runtime: 81ms
    Memory: 10.7 MB
    Time Complexity: O(n)
    Space Complexity: O(n)
    n is the length of `preorder` and `inorder`.
    """
    preorder_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {}

        for i in range(len(inorder)):
            hash_map[inorder[i]] = i

        return self.buildTreeHelper(preorder, 0, len(inorder) - 1, hash_map)

    def buildTreeHelper(self, preorder: List[int], left: int, right: int, hash_map: Dict[int, int]) -> Optional[TreeNode]:
        if left > right:
            return None

        node = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1
        inorder_index = hash_map[node.val]
        node.left = self.buildTreeHelper(preorder, left, inorder_index - 1, hash_map)
        node.right = self.buildTreeHelper(preorder, inorder_index + 1, right, hash_map)

        return node