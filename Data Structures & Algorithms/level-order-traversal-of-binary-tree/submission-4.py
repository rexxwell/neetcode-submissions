from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Breadth First Search
    # Runtime: 180ms
    # Memory: 11.0 MB
    # Time Complexity: O(n)
    #   Because each node gets added to the `queue` once,
    #   and popped from the `queue` once
    #   where its children gets added in `O(1)` time.
    # Space Complexity:
    #   Worst Case: O(2^h) or O(n/2) = O(n)
    #       If the tree is full and perfect, the last level will have 2^h nodes.
    #   Average Case: O(n)
    #       If the tree is balanced.
    #   Best Case: O(1)
    #       If the the tree is skewed and each node has 1 children.
    # n is the number of nodes in the tree.
    # h is the height of the tree.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = deque([root])
        level_order = []

        while queue:
            number_of_nodes = len(queue)
            current_level = []

            for i in range(number_of_nodes):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_order.append(current_level)
        
        return level_order