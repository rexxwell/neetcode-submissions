# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    Depth First Search Pre-Traversal
    Runtime: 141ms
    Memory: 11.6 MB
    Time Complexity: O(n)
    Space Complexity: O(n)
    n is the number of nodes in the tree. 
    """
    i = 0
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        tree_serialization = []
        self.serializeHelper(root, tree_serialization)

        return ",".join(tree_serialization)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        tree_deserialization = data.split(",")
        root = self.deserializeHelper(tree_deserialization)

        return root

    def serializeHelper(self, curr: Optional[TreeNode], tree_serialization: List[str]) -> None:
        if not curr:
            tree_serialization.append("N")
        else:
            tree_serialization.append(str(curr.val))
            self.serializeHelper(curr.left, tree_serialization)
            self.serializeHelper(curr.right, tree_serialization)

    def deserializeHelper(self, tree_deserialization: List[str]) -> Optional[TreeNode]:
        if tree_deserialization[self.i] == "N":
            self.i += 1
            return None

        node = TreeNode(int(tree_deserialization[self.i]))
        self.i += 1
        node.left = self.deserializeHelper(tree_deserialization)
        node.right = self.deserializeHelper(tree_deserialization)
        
        return node