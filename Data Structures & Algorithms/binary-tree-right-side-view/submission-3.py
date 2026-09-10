from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Breadth First Search
    Runtime: 53ms
    Memory: 8.2 MB
    Time Complexity: O(n)
    Space Complexity:
        Best Case: O(1) auxiliary space, O(n) total space
            If the tree is skewed.
        Worst Case: O(n) auxiliary space, O(n) total space
            If the tree is balanced.
    n is the number of nodes in the tree.
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        queue = deque([root])
        result = []

        while queue:
            for i in range(len(queue) - 1):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
            right_side_node = queue.popleft()
            result.append(right_side_node.val)

            if right_side_node.left:
                queue.append(right_side_node.left)

            if right_side_node.right:
                queue.append(right_side_node.right)

        return result