from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Depth First Search (Recursion)
    # Runtime: 192ms
    # Memory: 11.5 MB
    # Time Complexity: O(V + E)
    # Space Complexity:
    #   Worst Case: O(V + E)
    #   Average Case: O(log(V + E))
    # V is the number of vertices in the tree.
    # E is the number of edges in the tree.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []

        if root == None:
            return level_order

        return self.levelOrderHelper(root, 0, level_order)
    
    def levelOrderHelper(self, curr: Optional[TreeNode], level: int, level_order: List[List[int]]) -> List[List[int]]:
        if level < len(level_order):
            level_order[level].append(curr.val)
        else:
            level_order.append([curr.val])
        
        if curr.left:
            self.levelOrderHelper(curr.left, level + 1, level_order)

        if curr.right:
            self.levelOrderHelper(curr.right, level + 1, level_order)

        return level_order