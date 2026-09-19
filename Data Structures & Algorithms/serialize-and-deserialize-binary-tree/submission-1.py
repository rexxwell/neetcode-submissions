from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    Breadth First Search
    Runtime: 80ms
    Memory: 11.6 MB
    Time Complexity: O(n)
    Space Complexity: O(m)
    n is the number of nodes in the tree.
    m is the length of `tree_serialization` and `tree_deserialization`.
    """
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""

        queue = deque([root])
        tree_serialization = []

        while queue:
            node = queue.popleft()

            if node == None:
                tree_serialization.append("N")
            else:
                tree_serialization.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(tree_serialization)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        i = 0
        tree_deserialization = data.split(",")
        root = TreeNode(int(tree_deserialization[i]))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            i += 1
            node_left_value = tree_deserialization[i]
            i += 1
            node_right_value = tree_deserialization[i]

            if node_left_value == "N":
                node.left = None
            else:
                node_left = TreeNode(int(node_left_value))
                node.left = node_left
                queue.append(node_left)
            
            if node_right_value == "N":
                node.right = None
            else:
                node_right = TreeNode(int(node_right_value))
                node.right = node_right
                queue.append(node_right)

        return root