"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Hash Map (Optimized)
    # Runtime: 204ms
    # Memory: 16.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n is the number of nodes in the linked list.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer_to_deep_copy = {None: None}
        curr = head

        while curr != None:
            pointer_to_deep_copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr != None:
            pointer_to_deep_copy[curr].next = pointer_to_deep_copy[curr.next]
            pointer_to_deep_copy[curr].random = pointer_to_deep_copy[curr.random]
            curr = curr.next
        
        return pointer_to_deep_copy[head]