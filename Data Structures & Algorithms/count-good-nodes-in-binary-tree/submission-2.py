# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Depth First Search
    Runtime: 273ms
    Memory: 25.0 MB
    Time Complexity: O(n)
    Space Complexity:
        Worst Case: O(n)
            If the tree is skewed, then there will be n call stack depth.
        Average/Best Case: O(logn)
            If the tree is balanced, then there will be log(n) call stack depth.
    n is the number of nodes in the tree.
    '''
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        return self.goodNodesHelper(root, root.val)

    
    def goodNodesHelper(self, curr: TreeNode, max_node_value: int) -> int:
        if curr == None:
            return 0

        is_good = 0

        if curr.val >= max_node_value:
            is_good = 1
            max_node_value = curr.val
        
        return is_good + self.goodNodesHelper(curr.left, max_node_value) + self.goodNodesHelper(curr.right, max_node_value)
            