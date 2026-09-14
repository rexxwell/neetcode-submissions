from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Breadth First Search
    Runtime: 112ms
    Memory: 12.5 MB
    Time Complexity: O(n)
    Space Complexity:
        Worst/Average Case: O(n)
            If the tree is balanced.
        Best Case: O(1)
            If the tree is skewed.
    n is the number of nodes in the tree.
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, lower_limit, upper_limit = queue.popleft()

            if not (lower_limit < node.val < upper_limit):
                return False
            
            if node.left:
                queue.append((node.left, lower_limit, node.val))
            
            if node.right:
                queue.append((node.right, node.val, upper_limit))

        return True