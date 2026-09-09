# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Depth First Search
    # Runtime: 48ms
    # Memory: 8.2 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Worst Case: O(n)
    #       If the tree is skewed, there will be n call stacks.
    #   Average Case: O(logn)
    #       If the tree is balanced, there will be logn call stacks.
    # n is the number of nodes in the tree.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        result = []
        curr = root
        my_set = set()
        level = 0

        return self.rightSideViewHelper(curr, result, my_set, level)

    def rightSideViewHelper(self, curr: Optional[TreeNode], result: List[int], my_set: set, level: int) -> List[int]:
        if curr == None:
            return result

        if level not in my_set:
            result.append(curr.val)
            my_set.add(level)
        
        self.rightSideViewHelper(curr.right, result, my_set, level + 1)
        self.rightSideViewHelper(curr.left, result, my_set, level + 1)

        return result
            