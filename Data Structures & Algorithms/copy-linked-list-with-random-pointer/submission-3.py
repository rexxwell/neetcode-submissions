"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Brute Force
    # Runtime: 316ms
    # Memory: 15.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n is the number of nodes in the linked list.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        linked_list = []
        curr = head

        while curr != None:
            linked_list.append(curr)
            curr = curr.next
        
        deep_copy = [None] * len(linked_list)
        node_dict = {None: None}

        for i in range(len(linked_list) - 1, -1, -1):
            node = linked_list[i]
            node_deep_copy = None

            if node.next == None:
                node_deep_copy = Node(node.val, None, node.random)
            else:
                node_deep_copy = Node(node.val, deep_copy[i + 1], node.random)
            
            node_dict[node] = node_deep_copy
            deep_copy[i] = node_deep_copy
        
        for node in deep_copy:
            node.random = node_dict[node.random]
        
        return deep_copy[0] if len(linked_list) != 0 else None