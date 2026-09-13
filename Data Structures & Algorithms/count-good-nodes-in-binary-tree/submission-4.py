from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Breadth-First Search
    Runtime: 156ms
    Memory: 25.5 MB
    Time Complexity: O(n)
    Space Complexity:
        Average/Worst Case: O(n)
            If the tree is balanced
        Best Case: O(1)
            If the tree is skewed.
    n is the number of nodes in the tree.
    '''
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        queue = deque([(root, root.val)])
        good_nodes = 0

        while queue:
            node, max_value = queue.popleft()

            if node.val >= max_value:
                good_nodes += 1
                max_value = node.val

            if node.left:
                queue.append((node.left, max_value))
            
            if node.right:
                queue.append((node.right, max_value))
            
        return good_nodes